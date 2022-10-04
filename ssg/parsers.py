from typing import List
from pathlib import Path

class Parser:
    extensions: List[str] = []

    def valid_extension(self, extension):
        return extension in self.extensions
    
    def parse(path: Path, source: Path, dest: Path):
        raise NotImplementedError
    
    def read(path):
        with open(path) as file:
            return file.read()
    
    def write(self, path, dest, content, ext = ".html"):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path) as file:
            return file.write(content)