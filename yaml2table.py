from  dict2table import dict2table
from yaml2dict import yaml2dict


def yaml2table(yaml_file):
    return dict2table(yaml2dict(yaml_file))
