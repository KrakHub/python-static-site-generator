from pathlib import Path


class Site:
    def __init__(self, source, dest):
        self._source = source.Path()
        self._dest = dest.Path()
    def create_dir(self, path):
        directory = (self._dest / Path.relative_to(self._source))
        Path.mkdir(directory,parents=True,exist_ok=True)
    def build(self):
        Path.mkdir(self._dest,parents=True,exist_ok=True)
        for path in self._source.rglob("*"):
            if path.isdir():
                self.create_dir(path)
        