# utils.py

class Utils:
    def clean_text(self, text):
        return text.strip().replace('\n', ' ')

    def remove_empty(self, lst):
        return [item for item in lst if item]

    def deduplicate(self, lst):
        return list(set(lst))

    def to_lowercase(self, lst):
        return [item.lower() for item in lst]

    def contains_keyword(self, lst, keyword):
        return [item for item in lst if keyword.lower() in item.lower()]

    def count_keywords(self, lst, keyword):
        return sum(1 for item in lst if keyword.lower() in item.lower())

    def find_longest(self, lst):
        return max(lst, key=len)

    def list_to_string(self, lst):
        return ' '.join(lst)

    def string_to_list(self, string):
        return string.split()

    def is_valid_email(self, text):
        return "@" in text and "." in text
