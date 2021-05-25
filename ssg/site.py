from pathlib import Path
import os


class Site:
    def __init__(self, source, dest, parsers=None):
        self.source = Path(source)
        self.dest = Path(dest)
        self.parsers = []

    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok= True)
    
    def build(self):
        self.dest.mkdir(parents=True, exist_ok= True)

        for path in source.rglob("*"):
            if Path.is_dir(path):
                self.create_dir(path)
            elif Path.is_file(path):
                self.run_parser(path)    
    
    def load_parser(self, extension):
        for parser in self.parsers:
            if parser.valid_extesion(extension):
                return parser
    
    def run_parser(self, path):
        parser = self.load_parser(Path.suffix(path))
        if not parser == None:
            parser.parse(path, source, dest)
        else:
            print("Not implemented.")
        
