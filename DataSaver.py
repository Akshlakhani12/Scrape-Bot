# data_saver.py
import json
import csv

class DataSaver:
    def save_to_csv(self, data, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(data)

    def save_to_json(self, data, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

    def save_to_txt(self, data, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            for item in data:
                f.write(str(item) + '\n')

    def save_to_html(self, data, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("<html><body>")
            for item in data:
                f.write(f"<p>{item}</p>")
            f.write("</body></html>")

    def save_single_string(self, text, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text)

    def save_dict_list(self, dict_list, filename):
        self.save_to_json(dict_list, filename)

    def append_to_txt(self, data, filename):
        with open(filename, 'a', encoding='utf-8') as f:
            for item in data:
                f.write(str(item) + '\n')

    def read_from_txt(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return f.readlines()

    def load_json(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)

    def read_csv(self, filename):
        with open(filename, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            return list(reader)
