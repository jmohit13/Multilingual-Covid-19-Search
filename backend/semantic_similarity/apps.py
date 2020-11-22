from __future__ import unicode_literals
import os
import numpy as np
import pandas as pd
import tensorflow_hub as hub
from django.conf import settings
from django.apps import AppConfig
from laserembeddings import Laser

class AppConfig(AppConfig):
    name = "semantic_similarity"
    laser = Laser()
    model = hub.load(settings.USE_MODULE_URL)
    df = pd.read_csv(
        os.path.join(settings.ROOT_DIR, settings.SEMANTIC_SIMILARITY_DATA_FN)
    )
    BASE_VECTORS_LOADED = np.load(
        os.path.join(settings.ROOT_DIR, settings.BASE_VECTORS_FN), allow_pickle=True
    )
    PROCESSED_DATA_LOADED = np.load(
        os.path.join(settings.ROOT_DIR, settings.PROCESSED_DATA_FN), allow_pickle=True
    )
