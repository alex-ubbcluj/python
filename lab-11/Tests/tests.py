from Domain.client_validator import ClientValidator
from Repository.json_repository import JsonRepository
from Service.client_service import ClientService
from Tests.utils_tests import clear_file


def test_all():
    test_adauga_client()


def test_adauga_client():
    clear_file("Tests/test-clienti.json")
    client_repository = JsonRepository("Tests/test-clienti.json")
    client_validator = ClientValidator()
    client_service = ClientService(client_repository, client_validator)
    client_service.adauga("1", "nume1", "3678924561287", 257.76)
    client_service.adauga("2", "nume2", "4678934561485", 56.25)

    clienti = client_service.get_all()
    assert len(clienti) == 2
    assert clienti[0].id_entity == "1"
    assert clienti[0].nume == "nume1"
    assert len(clienti[0].cnp) == 13
    assert clienti[1].id_entity == "2"
    assert clienti[1].nume == "nume2"
    assert len(clienti[1].cnp) == 13
