from Domain.client import Client
from Domain.client_validator import ClientValidator
from Repository.json_repository import JsonRepository


class ClientService:
    def __init__(self, client_repository: JsonRepository,
                 client_validator: ClientValidator):
        self.client_repository = client_repository
        self.client_validator = client_validator

    def get_all(self):
        return self.client_repository.read()

    def adauga(self, id_client: str, nume: str, cnp: str, sold_initial: float):
        """
        Adauga un client in multimea de clienti
        :param id_client: id-ul clientului
        :param nume: numele clientului
        :param cnp: cnp-ul clientului
        :param sold_initial: soldul initial
        :return:
        """
        client = Client(id_client, nume, cnp, sold_initial)
        self.client_validator.validate(client)
        self.client_repository.create(client)

    def ordoneaza_descrescator_numar_vocale(self):
        """
         Ordoneaza descrescător clienții după numărul de vocale din nume
        :return: o lista de dictionare ordonata descrescator,
        ce contine fiecare client si numarul de vocale din numele acestuia
        """
        rezultat = []
        vocale = ['a', 'e', 'i', 'o', 'u']
        for client in self.client_repository.read():
            nume = client.nume
            nr_vocale = 0
            for litera in nume:
                if litera in vocale:
                    nr_vocale = nr_vocale + 1
            rezultat.append({"client": client, "vocale": nr_vocale})
        return sorted(rezultat, key=lambda x: x["vocale"], reverse=True)
