import jsonpickle
from Domain.entitate import Entitate
from Repository.repository_in_memory import RepositoryInMemory


class RepositoryJson(RepositoryInMemory):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def __read_file(self):
        try:
            with open(self.filename, "r") as f:
                return jsonpickle.loads(f.read())
        except Exception:
            return {}

    def __write_file(self):
        with open(self.filename, "w") as f:
            f.write(jsonpickle.dumps(self.entitati))

    def read(self, id_entitate=None):
        self.entitati = self.__read_file()
        return super().read(id_entitate)

    def add(self, entitate: Entitate):
        self.entitati = self.__read_file()
        super().add(entitate)
        self.__write_file()

    def delete(self, id_entitate):
        self.entitati = self.__read_file()
        super().delete(id_entitate)
        self.__write_file()

    def update(self, entitate: Entitate):
        self.entitati = self.__read_file()
        super().update(entitate)
        self.__write_file()
