from Domain.entitate import Entitate
from Repository.repository import Repository


class RepositoryInMemory(Repository):
    def __init__(self):
        self.entitati = {}

    def read(self, id_entitate=None):
        """
        param id_entitate (optional): id-ul entitatii despre care vrem detalii
        return: entitatea cu id-ul dat;
                None daca id-ul nu exista;
                o lista cu toate entitatile, daca id-ul nu este specificat
        """
        if id_entitate is None:
            return list(self.entitati.values())
        elif id_entitate in self.entitati:
            return self.entitati[id_entitate]
        else:
            return None

    def add(self, entitate: Entitate):
        """
        Adauga o entitate in entitati
        :param entitate: entitatea de adaugat
        :return: entitati, dupa adaugarea entitatii date
        """
        if self.read(entitate.id_entitate) is not None:
            raise KeyError("Exista deja o entitate cu id-ul dat!")
        self.entitati[entitate.id_entitate] = entitate

    def delete(self, id_entitate):
        """
        Sterge o entitate din entitati
        :param id_entitate: id-ul entitatii de sters
        :return: entitati, dupa stergerea entitatii cu id-ul dat
        """
        if self.read(id_entitate) is None:
            raise KeyError("Nu exista entitatea cu id-ul dat!")
        del self.entitati[id_entitate]

    def update(self, entitate: Entitate):
        """
        Modifica o entitate din entitati
        :param entitate: entitatea de modificat
        :return: entitati, dupa modificarea entitatii date
        """
        if self.read(entitate.id_entitate) is None:
            raise KeyError("Nu exista entitatea cu id-ul dat!")
        self.entitati[entitate.id_entitate] = entitate
