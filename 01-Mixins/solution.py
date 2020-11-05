import csv
import pickle
import json
import xml.etree.ElementTree as ET


class Serializable:
    def dump(self, path: str):
        with open(path, 'wb') as f:
            pickle.dump(self.__dict__, f, pickle.HIGHEST_PROTOCOL)

    def load(self, path: str):
        with open(path, 'rb') as f:
            tmp_dict = pickle.load(f)
            self.__dict__.update(tmp_dict)
            return self


class CSVMixin:
    def dump(self, path: str):
        attr_names = []
        for key in self.__dict__.keys():
            attr_names.append(key)

        with open(path, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=attr_names)
            writer.writeheader()
            writer.writerow(self.__dict__)

    def load(self, path: str):
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.__dict__.update(row)


class JSONMixin:
    def dump(self, path: str):
        with open(path, 'w') as f:
            json.dump(self.__dict__, f)

    def load(self, path: str):
        with open(path, 'r') as f:
            tmp_dict = json.load(f)
            self.__dict__.update(tmp_dict)
            return self


class XMLMixin:
    def dump(self, path: str):
        data = ET.Element('book')
        for key, value in self.__dict__.items():
            element = ET.SubElement(data, key)
            if isinstance(value, int):
                element.set('type', 'int')
            elif isinstance(value, float):
                element.set('type', 'float')
            else:
                element.set('type', 'str')
            element.text = str(value)

        b_xml = ET.tostring(data)
        with open(path, 'wb') as f:
            f.write(b_xml)

    def load(self, path: str):
        tree = ET.parse(path)
        root = tree.getroot()

        book_dict = {}
        for idx in range(len(root)):
            leaf = root[idx]
            book_dict[leaf.tag] = leaf.text

        self.__dict__.update(book_dict)
        return self
