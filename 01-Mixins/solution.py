import csv
import pickle


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
        pass

    def load(self, path: str):
        pass


class XMLMixin:
    def dump(self, path: str):
        pass

    def load(self, path: str):
        pass

