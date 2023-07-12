import json

class FileJsonConfig:
    def __init__(self):
        self.filename = "list_news.json"
        #self.load_config()

    def load_config(self):
        with open(self.filename, "r") as f:
            return json.load(f)