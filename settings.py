# -*- coding:utf-8 -*-
import os

BASE_URL = 'http://127.0.0.1:8000'

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

DATABASES_FOLDER = os.path.join(ROOT_PATH, 'databases')
print(DATABASES_FOLDER)

DATABASES_CONFIG = {
    'sqlite': f'sqlite:///{DATABASES_FOLDER}/blog.db'
}
