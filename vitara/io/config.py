"""
Does some global config
"""

import yaml
import matplotlib


def read_yml(filename: str):
    """
    Reads the yml file at filename into an object
    """

    with open(filename, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def setup(absolute_filename: str):
    config = read_yml(absolute_filename)
    if "matplotlib" not in config:
        raise ValueError("Config requires matplotlib config section")

    mpl_config = config.get("matplotlib")
    for key in mpl_config:
        matplotlib.rcParams[key] = mpl_config[key]
