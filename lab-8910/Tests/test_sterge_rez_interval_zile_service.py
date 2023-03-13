from datetime import datetime
from Domain.film_validator import FilmValidator
from Domain.rezervare import Rezervare
from Repository.repository_in_memory import RepositoryInMemory
from Repository.repository_json import RepositoryJson
from Service.card_client_service import CardClientService
from Service.film_service import FilmService
from Service.rezervare_service import RezervareService
from Service.undo_redo_service import UndoRedoService
from Tests.utils_tests import clear_file


def test_sterge_rez_interval_zile():
    filename = "Tests/test_sterge_rez_interval_zile.json"
    clear_file(filename)
    undo_redo_test = UndoRedoService()
    film_validator = FilmValidator()
    film_repository = RepositoryInMemory()
    film_service = FilmService(film_repository,
                               film_validator,
                               undo_redo_test)
    card_client_repository = RepositoryInMemory()
    card_client_service = CardClientService(card_client_repository,
                                            undo_redo_test)
    rezervare_repository = RepositoryJson(filename)
    rezervare_service = RezervareService(film_repository,
                                         card_client_repository,
                                         rezervare_repository,
                                         undo_redo_test)
    film_service.add("1", "Batman", "2009", 20.00, "da")
    film_service.add("2", "Joker", "2019", 30.00, "da")
    card_client_service.add("1", "Popescu", "Ionela", "6110211055573",
                            datetime(2011, 2, 11), datetime(2020, 9, 2), 0)
    card_client_service.add("2", "Ionescu", "George", "5010510079105",
                            datetime(2001, 5, 10), datetime(2021, 1, 7), 0)
    rezervare_service.add("1", "1", None, datetime(2012, 12, 12), 10.00)
    rezervare_service.add("2", "1", "1", datetime(2015, 9, 14), 13.30)
    rezervare_service.add("3", "2", "2", datetime(2017, 11, 23), 12.45)
    rezervare_service.sterge_rez_interval_zile(14, 22)
    assert rezervare_service.get_all() == \
           [Rezervare(id_entitate='1',
                      id_film='1',
                      id_card_client=None,
                      data=datetime(2012, 12, 12),
                      ora=10.0),
           Rezervare(id_entitate='3',
                     id_film='2',
                     id_card_client='2',
                     data=datetime(2017, 11, 23),
                     ora=12.45)]
