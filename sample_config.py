import os


class Config(object):
    REMOVEBG_API = os.environ.get("REMOVEBG_API", "")
