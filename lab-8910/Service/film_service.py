import random
import string
from functools import reduce
from Domain.add_operation import AddOperation
from Domain.delete_operation import DeleteOperation
from Domain.film import Film
from Domain.film_validator import FilmValidator
from Domain.update_operation import UpdateOperation
from Repository.repository import Repository
from Repository.repository_json import RepositoryJson
from Service.undo_redo_service import UndoRedoService


class FilmService:
    def __init__(self,
                 film_repository: Repository,
                 film_validator: FilmValidator,
                 undo_redo_service: UndoRedoService):
        self.__film_repository = film_repository
        self.__film_validator = film_validator
        self.__undo_redo_service = undo_redo_service

    def get_all(self):
        return self.__film_repository.read()

    def add(self, id_film, titlu, an_aparitie, pret_bilet, in_program):
        film = Film(id_film, titlu, an_aparitie, pret_bilet, in_program)
        self.__film_validator.validate(film)
        self.__film_repository.add(film)
        self.__undo_redo_service.add_undo_operation(AddOperation(
            self.__film_repository, film))

    def delete(self, id_film):
        film_sters = self.__film_repository.read(id_film)
        self.__film_repository.delete(id_film)
        self.__undo_redo_service.add_undo_operation(DeleteOperation(
            self.__film_repository, film_sters))

    def update(self, id_film, titlu, an_aparitie, pret_bilet, in_program):
        film_vechi = self.__film_repository.read(id_film)
        film = Film(id_film, titlu, an_aparitie, pret_bilet, in_program)
        self.__film_validator.validate(film)
        self.__film_repository.update(film)
        self.__undo_redo_service.add_undo_operation(UpdateOperation(
            self.__film_repository, film_vechi, film))

    def genereaza_filme_random(self, n):
        filme_generate = 0
        while filme_generate < n:
            id_film = str(random.randint(1, 999))
            titlu_list = []
            for lungime_titlu in range(random.randint(5, 10)):
                litera = random.choice(string.ascii_lowercase)
                titlu_list.append(litera)
            titlu = reduce(lambda x, y: str(x) + str(y), titlu_list)
            an_aparitie = str(random.randint(1930, 2021))
            pret_bilet = round(random.uniform(5.0, 39.99), 2)
            in_program_choices = ["da", "nu"]
            in_program = random.choice(in_program_choices)
            film = Film(id_film, titlu, an_aparitie, pret_bilet, in_program)
            if self.__film_repository.read(id_film) is not None:
                filme_generate = filme_generate - 1
            else:
                self.__film_repository.add(film)
            filme_generate = filme_generate + 1

    def cautare_film(self, search_str):
        return filter(lambda film:
                      search_str in film.id_entitate or
                      search_str in film.titlu or
                      search_str in film.an_aparitie or
                      search_str in str(film.pret_bilet) or
                      search_str in film.in_program,
                      self.__film_repository.read())

    def sterge_in_cascada(self, id_film):
        rezervari = RepositoryJson("rezervari.json")
        [rezervari.delete(rezervare.id_entitate)
         for rezervare in rezervari.read()
         if rezervare.id_film == id_film]
        self.__film_repository.delete(id_film)
