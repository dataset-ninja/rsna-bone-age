Dataset **RSNA Bone Age 2017** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/X/r/0P/XFjtEnZAZMBI5TJDuGa5uuNRZ4kJMTB3prlIq2R4O8IzG7qUHXfTBhXEep6aghtozGlrUMAWq93GXJcvYIuS7PX8uwh9EjRA5iO11Xg4iZbLpDqcVjCUklrmoOfk.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='RSNA Bone Age 2017', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be downloaded here:

- [Dataset description](https://www.rsna.org/-/media/Files/RSNA/Education/AI%20resources%20and%20training/AI%20image%20challenge/RSNA-2017-Pediatric-Bone-Age-Challenge-Dataset-Description.ashx?la=en&hash=A0B423007088816AFFACDCA934E2F09F903215F4&hash=A0B423007088816AFFACDCA934E2F09F903215F4)
- [Download training dataset (9.6 GB)](https://s3.amazonaws.com/east1.public.rsna.org/AI/2017/Bone+Age+Training+Set.zip)
- [Download training dataset annotations](https://s3.amazonaws.com/east1.public.rsna.org/AI/2017/Bone+Age+Training+Set+Annotations.zip)
- [Download validation dataset (1.1 GB)](https://s3.amazonaws.com/east1.public.rsna.org/AI/2017/Bone+Age+Validation+Set.zip)
