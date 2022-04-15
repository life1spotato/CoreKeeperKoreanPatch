import os

from glob import glob
import yaml

class YAMLDict:
    def __init__(self):
        with open('config.yaml') as f:
            self.data = yaml.load(f, Loader=yaml.FullLoader)

    def __getattr__(self, name):
        return self.data.get(name)

cfg = YAMLDict()

def get_json_path(dir, name):
    return glob(os.path.join(dir, '{}*.json'.format(name)))[0]