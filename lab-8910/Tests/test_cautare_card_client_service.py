from datetime import datetime
from Domain.card_client import CardClient
from Repository.repository_json import RepositoryJson
from Service.card_client_service import CardClientService
from Service.undo_redo_service import UndoRedoService
from Tests.utils_tests import clear_file


def test_cautare_card_client():
    filename = "Tests/test_cautare_card_client.json"
    clear_file(filename)
    carduri_clienti = RepositoryJson(filename)
    card_client_1 = CardClient("1", "Popescu", "Ionela", "6110211055573",
                               datetime(2011, 2, 11), datetime(2020, 9, 2), 34)
    carduri_clienti.add(card_client_1)
    card_client_2 = CardClient("2", "Ionescu", "George", "5010510079105",
                               datetime(2001, 5, 10), datetime(2021, 1, 7), 17)
    carduri_clienti.add(card_client_2)
    undo_redo_test = UndoRedoService()
    cautare_card_client = CardClientService(carduri_clienti, undo_redo_test)
    assert list(cautare_card_client.cautare_card_client("34")) == \
           [card_client_1]
    assert list(cautare_card_client.cautare_card_client("22")) == []
    assert list(cautare_card_client.cautare_card_client("escu")) == \
           [card_client_1, card_client_2]
