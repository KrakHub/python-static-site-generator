from json import load
import re
from yaml import FullLoader
from yaml import load
from collections.abc import Mapping

class Content(Mapping):
    def __init__(self):
        __delimiter = r"^(?:-|\+){3}\s*$"
        __regex = re.compile(__delimiter, re.MULTILINE)

    #def load(self, cls, string):
        