from dataclasses import dataclass
from datetime import date
from Domain.entitate import Entitate


@dataclass
class CardClient(Entitate):
    """
    Descrie cardul unui client
    """
    nume: str
    prenume: str
    cnp: str
    data_nasterii: date
    data_inregistrarii: date
    puncte_acumulate: int

    def __str__(self):
        return f"Card client: ID card client: {self.id_entitate}, " \
               f"nume: {self.nume}, " \
               f"prenume: {self.prenume}, " \
               f"CNP: {self.cnp}, " \
               f"data nasterii: {self.data_nasterii.strftime('%d.%m.%Y')}, " \
               f"data inregistrarii: " \
               f"{self.data_inregistrarii.strftime('%d.%m.%Y')}, " \
               f"puncte acumulate: {self.puncte_acumulate}"
