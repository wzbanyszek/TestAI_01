import json

class LanguageManager:
    def __init__(self):
        self.languages = {'en': {}, 'pl': {}, 'ru': {}}
        self.current_language = 'en'

    def load_dictionary(self, lang_code, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                self.languages[lang_code] = json.load(f)
        except FileNotFoundError:
            print(f"File {file_path} not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON.")

    def get_translations(self, key):
        return {lang: self.languages[lang].get(key, key) for lang in self.languages}

    def set_language(self, lang_code):
        if lang_code in self.languages:
            self.current_language = lang_code
        else:
            print(f"Language {lang_code} not supported.")

    def translate(self, key):
        return self.languages[self.current_language].get(key, key)