import json


class FileRepository:
    def __init__(self,
                 file_path: str,
                 is_json: bool = True):
        self.file_path = file_path
        self.is_json = is_json
        self.app_content = []
        self._init_app_content()

    def _init_app_content(self):
        self.app_content = self.load_from_file()

    # Create
    def save_to_file(self, content):
        if self.is_json:
            self._save_to_json(content)
        else:
            self._save_to_txt(content)

    def _save_to_json(self, content):
        # Provjeru je li content dict ili List[Dict] ili objekt ili lista objekata
        if isinstance(content, list):
            content = list(map(lambda x: x.__dict__, content))
            self.app_content.extend(content)
        else:
            content = content.__dict__
            self.app_content.append(content)

        try:
            with open(self.file_path, 'w') as file_writer:
                json.dump(self.app_content, file_writer, indent=4)

        except Exception as ex:
            print(f'Dogodila se greska {ex}.')

    def _save_to_txt(self, content):
        try:
            with open(self.file_path, 'a') as file_writer:
                file_writer.write(str(content) + '\n')

        except Exception as ex:
            print(f'Dogodila se greska {ex}.')

    # Read
    def load_from_file(self):
        if self.is_json:
            return self._load_from_json()
        else:
            self._load_from_text()

    def _load_from_json(self):
        try:
            with open(self.file_path, 'r') as file_reader:
                json_content = json.load(file_reader)
                return json_content
        except Exception as ex:
            print(f'Dogodila se greska {ex}.')

    def _load_from_text(self):
        # TODO Refactor!!!
        try:
            with open(self.file_path, 'r') as file_reader:
                self.app_content = file_reader.readlines()

        except Exception as ex:
            print(f'Dogodila se greska {ex}.')


    # Update

    # Delete
