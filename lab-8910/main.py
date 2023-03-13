from Domain.film_validator import FilmValidator
from Repository.repository_json import RepositoryJson
from Service.card_client_service import CardClientService
from Service.film_service import FilmService
from Service.rezervare_service import RezervareService
from Service.undo_redo_service import UndoRedoService
from Tests.test_all import test_all
from UI.console import Console


def main():
    undo_redo_service = UndoRedoService()
    film_validator = FilmValidator()
    film_repository_json = RepositoryJson("filme.json")
    film_service = FilmService(film_repository_json,
                               film_validator,
                               undo_redo_service)
    card_client_repository_json = RepositoryJson("carduri_clienti.json")
    card_client_service = CardClientService(card_client_repository_json,
                                            undo_redo_service)
    rezervare_repository_json = RepositoryJson("rezervari.json")
    rezervare_service = RezervareService(film_repository_json,
                                         card_client_repository_json,
                                         rezervare_repository_json,
                                         undo_redo_service)
    console = Console(film_service, card_client_service,
                      rezervare_service, undo_redo_service)

    test_all()
    console.run_meniu()


if __name__ == "__main__":
    main()
