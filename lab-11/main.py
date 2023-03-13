from Domain.client_validator import ClientValidator
from Domain.tranzactie_validator import TranzactieValidator
from Repository.json_repository import JsonRepository
from Service.client_service import ClientService
from Service.tranzactie_service import TranzactieService
from Tests.tests import test_all
from UserInterface.console import Console


def main():
    client_repository = JsonRepository("clienti.json")
    client_validator = ClientValidator()
    client_service = ClientService(client_repository, client_validator)
    tranzactie_repository = JsonRepository("tranzactii.json")
    tranzactie_validator = TranzactieValidator()
    tranzactie_service = TranzactieService(tranzactie_repository,
                                           tranzactie_validator,
                                           client_repository)
    console = Console(client_service, tranzactie_service)
    console.run_meniu()


if __name__ == '__main__':
    test_all()
    main()
