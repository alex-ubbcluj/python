from datetime import datetime
from Domain.film_validator import FilmValidator
from Repository.repository_in_memory import RepositoryInMemory
from Service.card_client_service import CardClientService
from Service.film_service import FilmService
from Service.rezervare_service import RezervareService
from Service.undo_redo_service import UndoRedoService


def test_undo_redo():
    undo_redo_test = UndoRedoService()
    film_validator = FilmValidator()
    film_repository = RepositoryInMemory()
    film_service = FilmService(film_repository,
                               film_validator,
                               undo_redo_test)
    card_client_repository = RepositoryInMemory()
    card_client_service = CardClientService(card_client_repository,
                                            undo_redo_test)
    rezervare_repository = RepositoryInMemory()
    rezervare_service = RezervareService(film_repository,
                                         card_client_repository,
                                         rezervare_repository,
                                         undo_redo_test)
    film_service.add("1", "Batman", "2009", 20.00, "da")
    film_service.add("2", "Joker", "2019", 30.00, "da")
    assert len(film_service.get_all()) == 2
    undo_redo_test.undo()
    assert len(film_service.get_all()) == 1
    undo_redo_test.redo()
    assert len(film_service.get_all()) == 2
    card_client_service.add("1", "Popescu", "Ionela", "6110211055573",
                            datetime(2011, 2, 11), datetime(2020, 9, 2), 0)
    card_client_service.add("2", "Ionescu", "George", "5010510079105",
                            datetime(2001, 5, 10), datetime(2021, 1, 7), 0)
    assert len(card_client_service.get_all()) == 2
    undo_redo_test.undo()
    assert len(card_client_service.get_all()) == 1
    undo_redo_test.redo()
    rezervare_service.add("1", "1", "1", datetime(2022, 1, 9), 21.45)
    rezervare_service.add("2", "2", "2", datetime(2021, 12, 30), 14.15)
    assert len(rezervare_service.get_all()) == 2
    undo_redo_test.undo()
    assert len(rezervare_service.get_all()) == 1
    undo_redo_test.redo()
    rezervare_service.sterge_rez_interval_zile(10, 30)
    assert len(rezervare_service.get_all()) == 1
    undo_redo_test.undo()
    assert len(rezervare_service.get_all()) == 2
    card_client_service.incrementare_puncte_interval_zile(10, 11, 3)
    card_client_1 = card_client_repository.read("1")
    card_client_2 = card_client_repository.read("2")
    assert card_client_1.puncte_acumulate == 5
    assert card_client_2.puncte_acumulate == 6
    undo_redo_test.undo()
    assert card_client_1.puncte_acumulate == 2
    assert card_client_2.puncte_acumulate == 3
    card_client_service.delete("1")
    assert card_client_repository.read("1") is None
    card_client_service.incrementare_puncte_interval_zile(1, 31, 10)
    assert card_client_2.puncte_acumulate == 13
    undo_redo_test.redo()
    assert card_client_repository.read("1") is None
    assert card_client_2.puncte_acumulate == 13
    undo_redo_test.undo()
    assert card_client_2.puncte_acumulate == 3
