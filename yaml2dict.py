"""
deals with the yaml file
"""
import yaml


def yaml2dict(afile):
    return yaml.load(afile)


