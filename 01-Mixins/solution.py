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


class CSVMixin:
    def dump(self, path: str):
        pass

    def load(self, path: str):
        pass
