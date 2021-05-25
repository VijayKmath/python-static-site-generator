from typing import List
from pathlib import Path
import shutil


class Parser:
    extensions = []
    extensions = List[str]

    def valid_extension(self, extension):
        if extension in self.extensions:
            return True
        
        return False
    
    def parser(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError
    
    def read(self, path):
        with open(path) as file:
            return file.read()

    def write(self, path, dest, content, ext=".html"):
        full_path =self.dest / path.with_suffix(ext).name
        with open(full_path) as file:
            file.write(content)
    
    def copy(self, path, source, dest):
        dest2 = dest / path.relative_to(source)
        shutil.copy2(path, dest2)

    class ResourceParser:
        extensions = [".jpg", ".png", ".gif", ".css", ".html"]

        def parse(self, path: Path, source: Path, dest: Path):
            copy(self, path, source, dest)


