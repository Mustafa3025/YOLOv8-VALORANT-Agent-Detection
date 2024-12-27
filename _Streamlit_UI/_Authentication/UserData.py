from pathlib import Path
import json

class UserData:

    def __init__(self, file_path = "_Authentication/credentials.json"):
        self.file_path = Path(file_path)

    def load_user_data(self):
        if not self.file_path.exists():
            self.file_path.write_text(json.dumps({}), encoding = "utf-8")
        return json.loads(self.file_path.read_text(encoding = "utf-8"))
    
    def save_user_data(self, data):
        self.file_path.write_text(json.dumps(data, indent = 4), encoding = "utf-8")
        