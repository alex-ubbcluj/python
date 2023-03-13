import jsonpickle
from Domain.tranzactie import Tranzactie
from Domain.tranzactie_validator import TranzactieValidator
from Repository.json_repository import JsonRepository


class TranzactieService:
    def __init__(self, tranzactie_repository: JsonRepository,
                 tranzactie_validator: TranzactieValidator,
                 client_repository: JsonRepository):
        self.tranzactie_repository = tranzactie_repository
        self.tranzactie_validator = tranzactie_validator
        self.client_repository = client_repository

    def get_all(self):
        return self.tranzactie_repository.read()

    def adauga(self, id_tranzactie: str, id_client_sursa: str,
               id_client_destinatie: str, valoare: float):
        """
        Adauga o tranzactie in multimea de tranzactii
        :param id_tranzactie: id-ul tranzactiei
        :param id_client_sursa: id-ul clientului sursa
        :param id_client_destinatie: id-ul clientului destinatie
        :param valoare: valaorea tranzactiei
        :return:
        """
        tranzactie = Tranzactie(id_tranzactie, id_client_sursa,
                                id_client_destinatie, valoare)
        self.tranzactie_validator.validate(tranzactie)
        if self.client_repository.read(id_client_sursa) is None:
            raise KeyError("Nu exista clientul sursa!")
        if self.client_repository.read(id_client_destinatie) is None:
            raise KeyError("Nu exista clientul destinatie!")
        client_sursa = self.client_repository.read(id_client_sursa)
        if valoare > client_sursa.sold_initial:
            raise ValueError("Solduri insuficiente "
                             "pentru a efectua tranzactia!")
        self.tranzactie_repository.create(tranzactie)
        client_destinatie = self.client_repository.read(id_client_destinatie)
        client_sursa.sold_initial -= valoare
        self.client_repository.update(client_sursa)
        client_destinatie.sold_initial += valoare
        self.client_repository.update(client_destinatie)

    def determina_tranzactii_periculoase(self):
        """
        Determina toate tranzactiile periculoase
        :return: o lista de dictionare ce contin valorile cerute
        """
        tranzactii_periculoase = []
        for tranzactie in self.tranzactie_repository.read():
            if tranzactie.valoare > 15000:
                tranzactii_periculoase.append(tranzactie)
        rezultat = []
        for tranzactie in tranzactii_periculoase:
            client_sursa = \
                self.client_repository.read(tranzactie.id_client_sursa)
            client_destinatie = \
                self.client_repository.read(tranzactie.id_client_destinatie)
            rezultat.append({"tranzactie": tranzactie,
                             "nume sursa": client_sursa.nume,
                             "CNP sursa": client_sursa.cnp,
                             "nume destinatie": client_destinatie.nume,
                             "CNP destinatie": client_destinatie.cnp})
        return rezultat

    def export_json(self, cnp, filename):
        """
        Exporta istoricul tranzactiilor unui client, in format JSON
        :param cnp: CNP-ul clientului pentru care se va construi istoricul
        :param filename: numele fisierului
        in care se va face exportul istoricului
        :return:
        """
        rezultat = {}
        client_cautat = None
        for client in self.client_repository.read():
            if client.cnp == cnp:
                client_cautat = client
        if client_cautat is None:
            raise ValueError("Nu exista clientul cu CNP-ul dat!")
        for tranzactie in self.tranzactie_repository.read():
            if client_cautat.id_entity == tranzactie.id_client_sursa:
                client_destinatie = self.client_repository.read(
                    tranzactie.id_client_destinatie)
                rezultat[tranzactie.id_entity] = ("trimitere",
                                                  client_destinatie.nume,
                                                  tranzactie.valoare)
            elif client_cautat.id_entity == tranzactie.id_client_destinatie:
                client_sursa = \
                    self.client_repository.read(tranzactie.id_client_sursa)
                rezultat[tranzactie.id_entity] = ("primire",
                                                  client_sursa.nume,
                                                  tranzactie.valoare)
        with open(filename, 'w') as f:
            f.write(jsonpickle.dumps(rezultat))
