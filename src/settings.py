from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "RSNA Bone Age 2017"
PROJECT_NAME_FULL: str = "RSNA Pediatric Bone Age Challenge 2017"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.Custom(
    source_url="https://www.rsna.org/-/media/Files/RSNA/Education/AI-resources-and-training/AI-image-challenge/RSNA-2017-AI-Challenge-Terms-of-Use-and-Attribution_Final.ashx?la=en&hash=F28B401E267D05658C85F5D207EC4F9AE9AE6FA9"
)
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Medical()]
CATEGORY: Category = Category.Medical()

CV_TASKS: List[CVTask] = [CVTask.Identification()]
ANNOTATION_TYPES: List[AnnotationType] = []

RELEASE_DATE: Optional[str] = None  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = 2017

HOMEPAGE_URL: str = (
    "https://www.rsna.org/rsnai/ai-image-challenge/rsna-pediatric-bone-age-challenge-2017"
)
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 11729812
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/rsna-bone-age"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = {
    "Dataset description": "https://www.rsna.org/-/media/Files/RSNA/Education/AI%20resources%20and%20training/AI%20image%20challenge/RSNA-2017-Pediatric-Bone-Age-Challenge-Dataset-Description.ashx?la=en&hash=A0B423007088816AFFACDCA934E2F09F903215F4&hash=A0B423007088816AFFACDCA934E2F09F903215F4",
    "Download training dataset (9.6 GB)": "https://s3.amazonaws.com/east1.public.rsna.org/AI/2017/Bone+Age+Training+Set.zip",
    "Download training dataset annotations": "https://s3.amazonaws.com/east1.public.rsna.org/AI/2017/Bone+Age+Training+Set+Annotations.zip",
    "Download validation dataset (1.1 GB)": "https://s3.amazonaws.com/east1.public.rsna.org/AI/2017/Bone+Age+Validation+Set.zip",
}
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

# If you have more than the one paper, put the most relatable link as the first element of the list
# Use dict key to specify name for a button
PAPER: Optional[Union[str, List[str], Dict[str, str]]] = [
    "https://pubs.rsna.org/doi/10.1148/radiol.2018180736",
    "https://pubs.rsna.org/doi/10.1148/radiol.2018182657",
    "https://pubs.rsna.org/doi/10.1148/radiol.2017170236",
]
BLOGPOST: Optional[Union[str, List[str], Dict[str, str]]] = None
REPOSITORY: Optional[Union[str, List[str], Dict[str, str]]] = {
    "Kaggle": "https://www.kaggle.com/datasets/kmader/rsna-bone-age"
}

CITATION_URL: Optional[
    str
] = "https://www.rsna.org/-/media/Files/RSNA/Education/AI%20resources%20and%20training/AI%20image%20challenge/RSNA-2017-Pediatric-Bone-Age-Challenge-Dataset-Description.ashx?la=en&hash=A0B423007088816AFFACDCA934E2F09F903215F4&hash=A0B423007088816AFFACDCA934E2F09F903215F4"

AUTHORS: Optional[List[str]] = [
    "Safwan S. Halabi",
    "Luciano M. Prevedello",
    "Jayashree Kalpathy-Cramer",
    "Artem B. Mamonov",
    "Alexander Bilbily",
    "Mark Cicero",
    "Ian Pan",
    "Lucas Araújo Pereira",
    "Rafael Teixeira Sousa",
    "Nitamar Abdala",
    "Felipe Campos Kitamura",
    "Hans H. Thodberg",
    "Leon Chen",
    "George Shih",
    "Katherine Andriole",
    "Marc D. Kohli",
    "Bradley J. Erickson",
    "Adam E. Flanders",
]
AUTHORS_CONTACTS: Optional[List[str]] = ["safwan.halabi@stanford.edu"]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = "Radiological Society of North America"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "https://www.rsna.org/"

# Set '__PRETEXT__' or '__POSTTEXT__' as a key with string value to add custom text. e.g. SLYTAGSPLIT = {'__POSTTEXT__':'some text}
SLYTAGSPLIT: Optional[Dict[str, Union[List[str], str]]] = {"image splits": ["male", "female"]}
TAGS: Optional[List[str]] = None


SECTION_EXPLORE_CUSTOM_DATASETS: Optional[List[str]] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "project_name_full": PROJECT_NAME_FULL or PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["blog"] = BLOGPOST
    settings["repository"] = REPOSITORY
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    settings["explore_datasets"] = SECTION_EXPLORE_CUSTOM_DATASETS

    return settings
