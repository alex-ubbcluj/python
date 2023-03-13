from Domain.film import Film
from Domain.film_validator import FilmValidator
from Repository.repository_json import RepositoryJson
from Service.film_service import FilmService
from Service.undo_redo_service import UndoRedoService
from Tests.utils_tests import clear_file


def test_cautare_film():
    filename = "Tests/test_cautare_film.json"
    clear_file(filename)
    filme = RepositoryJson(filename)
    film_1 = Film("1", "Batman", "2009", 20.99, "da")
    filme.add(film_1)
    film_2 = Film("2", "Joker", "2019", 25.99, "da")
    filme.add(film_2)
    film_validator_test = FilmValidator()
    undo_redo_test = UndoRedoService()
    cautare_film = FilmService(filme, film_validator_test, undo_redo_test)
    assert list(cautare_film.cautare_film("Bat")) == [film_1]
    assert list(cautare_film.cautare_film("12345")) == []
    assert list(cautare_film.cautare_film("20")) == [film_1, film_2]
