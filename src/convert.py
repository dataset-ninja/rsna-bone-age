# https://www.kaggle.com/datasets/ardacanuckan/bone-classification-and-detection-dataset
import csv
import os
import shutil
from urllib.parse import unquote, urlparse

import numpy as np
import supervisely as sly
from dataset_tools.convert import unpack_if_archive
from dotenv import load_dotenv
from supervisely.io.fs import (
    dir_exists,
    file_exists,
    get_file_ext,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
    list_files_recursively,
)
from tqdm import tqdm

import src.settings as s


def count_files(path, extension):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # project_name = "bone classification and detection"
    train_path = (
        "/home/grokhi/rawdata/rsna-bone-age/boneage-training-dataset/boneage-training-dataset"
    )
    test_path = "/home/grokhi/rawdata/rsna-bone-age/boneage-test-dataset/boneage-test-dataset"
    val_path = "/home/grokhi/rawdata/rsna-bone-age/Bone Age Validation Set"

    dataset_path = "/home/grokhi/rawdata/rsna-bone-age/"
    images_ext = ".png"
    # ann_ext = ".txt"
    batch_size = 30

    ds_name_to_data = {"training": train_path, "validation": val_path, "test": test_path}

    def create_ann(image_path):
        labels = []
        tags = []

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        bonage, male = id_to_ann.get(get_file_name(image_path), (None, None))
        if bonage is not None:
            age_val = int(bonage)
            tags.append(sly.Tag(age_tag, value=age_val))

        if male is not None:
            tag_name = "male" if male == "true" else "female"
            tags += [sly.Tag(tag_meta) for tag_meta in tag_metas if tag_meta.name == tag_name]

        return sly.Annotation(img_size=(img_height, img_wight), img_tags=tags)

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)

    tag_names = ["male", "female"]
    age_tag = sly.TagMeta("boneage", sly.TagValueType.ANY_NUMBER)
    tag_metas = [sly.TagMeta(name, sly.TagValueType.NONE) for name in tag_names]

    meta = sly.ProjectMeta(tag_metas=[age_tag] + tag_metas)
    api.project.update_meta(project.id, meta.to_json())

    ann_paths = list_files_recursively(dataset_path, [".csv"])

    m_to_true = {"true": "true", "m": "true", "f": "false", "false": "false"}

    def csv_file_to_dict(filename):
        def safe_int(value):
            try:
                return int(value)
            except TypeError:
                return None

        with open(filename, "r") as file:
            reader = csv.DictReader(file, delimiter=",")
            if "validation" in filename.lower():
                head = ("Image ID", "Bone Age (months)", "male")
            if "training" in filename.lower():
                head = ("id", "boneage", "male")
            if "test" in filename.lower():
                head = ("Case ID", None, "Sex")

            _id, _boneage, _male = head
            data_dict = {
                row[_id]: [safe_int(row.get(_boneage)), m_to_true[row[_male].lower()]]
                for row in reader
            }

        return data_dict

    for ds_name, data_path in ds_name_to_data.items():
        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

        images_paths = list_files_recursively(data_path, [".png"])

        filename = [p for p in ann_paths if ds_name in p.lower()][0]
        id_to_ann = csv_file_to_dict(filename)

        progress = sly.Progress("Create dataset {}".format(ds_name), len(images_paths))

        for images_paths_batch in sly.batched(images_paths, batch_size=batch_size):
            images_names_batch = [
                get_file_name_with_ext(image_path) for image_path in images_paths_batch
            ]

            img_infos = api.image.upload_paths(dataset.id, images_names_batch, images_paths_batch)
            img_ids = [im_info.id for im_info in img_infos]

            anns = [create_ann(image_path) for image_path in images_paths_batch]
            api.annotation.upload_anns(img_ids, anns)

            progress.iters_done_report(len(images_names_batch))

    return project
