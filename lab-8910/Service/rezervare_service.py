from Domain.add_operation import AddOperation
from Domain.delete_operation import DeleteOperation
from Domain.multiple_delete_operation import MultiDeleteOperation
from Domain.rezervare import Rezervare
from Domain.update_operation import UpdateOperation
from MyFunctions.my_sorted import my_sorted
from Repository.repository import Repository
from Service.undo_redo_service import UndoRedoService


class RezervareService:
    def __init__(self, film_repository: Repository,
                 card_client_repository: Repository,
                 rezervare_repository: Repository,
                 undo_redo_service: UndoRedoService):
        self.__film_repository = film_repository
        self.__card_client_repository = card_client_repository
        self.__rezervare_repository = rezervare_repository
        self.__undo_redo_service = undo_redo_service

    def get_all(self):
        return self.__rezervare_repository.read()

    def add(self, id_rezervare, id_film, id_card_client, data, ora):
        if self.__film_repository.read(id_film) is None:
            raise ValueError("Nu exista filmul cu id-ul dat!")
        film_rez = self.__film_repository.read(id_film)
        if film_rez.in_program == "nu":
            raise ValueError("Nu puteti rezerva un film "
                             "care nu este in program!")
        if id_card_client is not None:
            if self.__card_client_repository.read(id_card_client) is not None:
                card_client = \
                    self.__card_client_repository.read(id_card_client)
                card_client.puncte_acumulate += int(film_rez.pret_bilet / 10)
                self.__card_client_repository.update(card_client)
            else:
                raise ValueError("Nu exista cardul cu id-ul dat! ")
        rezervare = Rezervare(id_rezervare, id_film, id_card_client, data, ora)
        self.__rezervare_repository.add(rezervare)
        self.__undo_redo_service.add_undo_operation(AddOperation(
            self.__rezervare_repository, rezervare))

    def delete(self, id_rezervare):
        rezervare_stearsa = self.__rezervare_repository.read(id_rezervare)
        self.__rezervare_repository.delete(id_rezervare)
        self.__undo_redo_service.add_undo_operation(DeleteOperation(
            self.__rezervare_repository, rezervare_stearsa))

    def update(self, id_rezervare, id_film, id_card_client, data, ora):
        rezervare_veche = self.__rezervare_repository.read(id_rezervare)
        if self.__film_repository.read(id_film) is None:
            raise ValueError("Nu exista filmul cu id-ul dat!")
        film_rez = self.__film_repository.read(id_film)
        if film_rez.in_program == "nu":
            raise ValueError("Nu puteti rezerva un film "
                             "care nu este in program!")
        if id_card_client is not None:
            if self.__card_client_repository.read(id_card_client) is None:
                raise ValueError("Nu exista cardul cu id-ul dat! ")
            if rezervare_veche.id_card_client != id_card_client:
                card_client = \
                    self.__card_client_repository.read(id_card_client)
                card_client.puncte_acumulate += int(film_rez.pret_bilet / 10)
                self.__card_client_repository.update(card_client)
        rezervare = Rezervare(id_rezervare, id_film, id_card_client, data, ora)
        self.__rezervare_repository.update(rezervare)
        self.__undo_redo_service.add_undo_operation(UpdateOperation(
            self.__rezervare_repository, rezervare_veche, rezervare))

    def rezervari_interval_orar(self, ora_inceput, ora_sfarsit):
        """
        Determina toate rezervarile dintr-un interval orar dat indiferent de zi
        param. ora_inceput: ora minima de la care pot incepe filmele cautate
        param. ora_sfarsit: ora maxima de la care pot incepe filmele cautate
        return: rezervarile din intervalul [ora_inceput, ora_sfarsit]
        """
        if ora_inceput > ora_sfarsit:
            raise ValueError("Ora de inceput nu poate fi mai mare "
                             "decat ora de sfarsit!")
        return [rezervare for rezervare in self.__rezervare_repository.read()
                if ora_inceput <= rezervare.ora <= ora_sfarsit]

    def ord_filme_dupa_nr_rez(self):
        nr_rez_list = []
        for film in self.__film_repository.read():
            numar_rezervari = 0
            nr_rez_list.append(numar_rezervari)
            for rezervare in self.__rezervare_repository.read():
                if rezervare.id_film == film.id_entitate:
                    numar_rezervari = numar_rezervari + 1
                    nr_rez_list.pop()
                    nr_rez_list.append(numar_rezervari)
        rezultat = list(zip(self.__film_repository.read(), nr_rez_list))
        return my_sorted(rezultat, key=lambda nr_rez: nr_rez[1], reverse=True)

    def sterge_rez_interval_zile(self, zi_start, zi_stop):
        """
        Șterge toate rezervările dintr-un anumit interval de zile
        param. zi_start: ziua minima de stergere
        param. zi_stop: ziua maxima de stergere
        return:
        """
        if zi_start > zi_stop:
            raise ValueError("Ziua de inceput nu poate fi mai mare "
                             "decat ziua de sfarsit!")
        self.__undo_redo_service.add_undo_operation(MultiDeleteOperation(
            self.__rezervare_repository,
            [rezervare for rezervare in self.__rezervare_repository.read()
             if zi_start <= rezervare.data.day <= zi_stop]))
        [self.__rezervare_repository.delete(rezervare.id_entitate)
         for rezervare in self.__rezervare_repository.read()
         if zi_start <= rezervare.data.day <= zi_stop]
