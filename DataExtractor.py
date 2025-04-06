# data_extractor.py

class DataExtractor:
    def get_text(self, elements):
        return [el.get_text(strip=True) for el in elements]

    def get_links(self, elements):
        return [el.get("href") for el in elements if el.get("href")]

    def get_images(self, elements):
        return [el.get("src") for el in elements if el.get("src")]

    def get_element_html(self, elements):
        return [str(el) for el in elements]

    def count_elements(self, elements):
        return len(elements)

    def get_attributes(self, elements, attr):
        return [el.get(attr) for el in elements if el.get(attr)]

    def filter_by_text(self, elements, keyword):
        return [el for el in elements if keyword.lower() in el.get_text().lower()]

    def get_classes(self, elements):
        return [el.get("class") for el in elements]

    def get_ids(self, elements):
        return [el.get("id") for el in elements]

    def tag_names(self, elements):
        return [el.name for el in elements]
