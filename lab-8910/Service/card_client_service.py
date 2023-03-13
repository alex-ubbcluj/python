import random
import string
from datetime import datetime
from functools import reduce
from Domain.add_operation import AddOperation
from Domain.card_client import CardClient
from Domain.delete_operation import DeleteOperation
from Domain.multiple_apply_function import MultiApplyFunction
from Domain.update_operation import UpdateOperation
from MyFunctions.my_sorted import my_sorted
from Repository.repository import Repository
from Service.undo_redo_service import UndoRedoService


class CardClientService:
    def __init__(self, card_client_repository: Repository,
                 undo_redo_service: UndoRedoService):
        self.__card_client_repository = card_client_repository
        self.__undo_redo_service = undo_redo_service

    def get_all(self):
        return self.__card_client_repository.read()

    def add(self,
            id_card_client,
            nume,
            prenume,
            cnp,
            data_nasterii,
            data_inregistrarii,
            puncte_acumulate):
        card_client = CardClient(id_card_client,
                                 nume,
                                 prenume,
                                 cnp,
                                 data_nasterii,
                                 data_inregistrarii,
                                 puncte_acumulate)
        for check_card_client in self.__card_client_repository.read():
            if check_card_client.cnp == card_client.cnp:
                raise ValueError("CNP-ul trebuie sa fie unic!")
        self.__card_client_repository.add(card_client)
        self.__undo_redo_service.add_undo_operation(AddOperation(
            self.__card_client_repository, card_client))

    def delete(self, id_card_client):
        card_client_sters = self.__card_client_repository.read(id_card_client)
        self.__card_client_repository.delete(id_card_client)
        self.__undo_redo_service.add_undo_operation(DeleteOperation(
            self.__card_client_repository, card_client_sters))

    def update(self,
               id_card_client,
               nume,
               prenume,
               cnp,
               data_nasterii,
               data_inregistrarii,
               puncte_acumulate):
        card_client_vechi = self.__card_client_repository.read(id_card_client)
        card_client = CardClient(id_card_client,
                                 nume,
                                 prenume,
                                 cnp,
                                 data_nasterii,
                                 data_inregistrarii,
                                 puncte_acumulate)
        for check_card_client in self.__card_client_repository.read():
            if check_card_client.cnp == card_client.cnp:
                raise ValueError("CNP-ul trebuie sa fie unic!")
        self.__card_client_repository.update(card_client)
        self.__undo_redo_service.add_undo_operation(UpdateOperation(
            self.__card_client_repository, card_client_vechi, card_client))

    def genereaza_carduri_random(self, n):
        carduri_generate = 0
        while carduri_generate < n:
            id_card_client = str(random.randint(1, 999))
            nume_list = []
            for lungime_nume in range(random.randint(5, 7)):
                litera = random.choice(string.ascii_lowercase)
                nume_list.append(litera)
            nume = reduce(lambda x, y: str(x) + str(y), nume_list)
            prenume_list = []
            for lungime_prenume in range(random.randint(5, 7)):
                litera = random.choice(string.ascii_lowercase)
                prenume_list.append(litera)
            prenume = reduce(lambda x, y: str(x) + str(y), prenume_list)
            cnp = str(random.randint(1000000000000, 9999999999999))
            data_nasterii = datetime(random.randint(1945, 2021),
                                     random.randint(1, 12),
                                     random.randint(1, 28))
            data_inregistrarii = datetime(random.randint(1945, 2021),
                                          random.randint(1, 12),
                                          random.randint(1, 28))
            card_client = CardClient(id_card_client,
                                     nume,
                                     prenume,
                                     cnp,
                                     data_nasterii,
                                     data_inregistrarii,
                                     0)
            if self.__card_client_repository.read(id_card_client) is not None:
                carduri_generate = carduri_generate - 1
            else:
                id_unic = True
                for check_card_client in self.__card_client_repository.read():
                    if check_card_client.cnp == card_client.cnp:
                        id_unic = False
                if id_unic is True:
                    self.__card_client_repository.add(card_client)
                else:
                    carduri_generate = carduri_generate - 1
            carduri_generate = carduri_generate + 1

    def cautare_card_client(self, search_str):
        return filter(lambda card_client:
                      search_str in card_client.id_entitate or
                      search_str in card_client.nume or
                      search_str in card_client.prenume or
                      search_str in card_client.cnp or
                      search_str in
                      card_client.data_nasterii.strftime("%d.%m.%Y") or
                      search_str
                      in card_client.data_inregistrarii.strftime("%d.%m.%Y") or
                      search_str in str(card_client.puncte_acumulate),
                      self.__card_client_repository.read())

    def ord_carduri_dupa_pct(self):
        """
        Ordoneaza descrescator cardurile client
        după numărul de puncte de pe card
        return: o lista cu toate cardurile ordonate corespunzator
        """
        return my_sorted(self.__card_client_repository.read(),
                         key=lambda card_client: card_client.puncte_acumulate,
                         reverse=True)

    def incrementare_puncte(self, card_client: CardClient, puncte):
        card_client.puncte_acumulate += puncte
        self.__card_client_repository.update(card_client)

    def incrementare_puncte_interval_zile(self, zi_start, zi_stop, puncte):
        """
        Incrementeaza cu o valoare dată punctele de pe toate cardurile
        a căror zi de naștere se află într-un interval dat
        param. zi_start: ziua de inceput
        param. zi_stop: ziua de sfarsit
        param. puncte: valoarea de incrementat
        return:
         """
        if zi_start > zi_stop:
            raise ValueError("Ziua de inceput nu poate fi mai mare "
                             "decat ziua de sfarsit!")
        if puncte < 0:
            raise ValueError("Incrementarea se poate face "
                             "doar cu o valoare pozitiva!")
        carduri_modificate = []
        for card_client in self.__card_client_repository.read():
            if zi_start <= card_client.data_nasterii.day <= zi_stop:
                carduri_modificate.append(card_client)
                self.incrementare_puncte(card_client, puncte)
        self.__undo_redo_service.add_undo_operation(MultiApplyFunction(
            self.incrementare_puncte, puncte, carduri_modificate))
