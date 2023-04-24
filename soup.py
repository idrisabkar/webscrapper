import requests
from bs4 import BeautifulSoup


class HTMLScraper:
    def __init__(self, url, page):
        self.url = url
        self.page = page
        self.soup = self._get_soup()

    def _get_soup(self):
        headers = {"page": str(self.page)}
        try:
            r = requests.get(self.url, headers=headers)
            return BeautifulSoup(r.content, "html.parser")
        except requests.exceptions.InvalidSchema as e:
            return "InvalidUrl"

    def find_elements(self, selector, value):
        """Find elements using the specified selector and value"""
        if self.soup == "InvalidUrl" :
            return ["Invalid Url!"]
        else:
            if selector == "tag_name":
                elements = self.soup.find_all(value)
                elements = [element.text for element in elements if element.text]
            elif selector == "id":
                element = self.soup.find(id=value)
                elements = [element.text] if element else []
            elif selector == "class_name":
                elements = self.soup.find_all(class_=value)
                elements = [element.text for element in elements if element.text]
            elif selector == "css_selector":
                elements = self.soup.select(value)
                elements = [element.text for element in elements if element.text]
            elif selector == "text":
                elements = self.soup.find_all(text=value)
                elements = [element for element in elements if element.strip()]
            elif selector == "attribute":
                attr_name, attr_value = value.split("=")
                elements = self.soup.find_all(attrs={attr_name: attr_value})
                elements = [element.text for element in elements if element.text]
            else:
                raise ValueError("Invalid selector: {}".format(selector))
            return elements
