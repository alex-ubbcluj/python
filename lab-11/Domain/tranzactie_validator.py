from Domain.tranzactie import Tranzactie


class TranzactieValidator:
    def validate(self, tranzactie: Tranzactie):
        if tranzactie.id_client_sursa == tranzactie.id_client_destinatie:
            raise ValueError("Clientul sursa si cel destinatie "
                             "trebuie sa fie diferiti!")
