from dataclasses import dataclass
from datetime import date
from Domain.entitate import Entitate


@dataclass
class Rezervare(Entitate):
    """
    Descrie o rezervare
    """
    id_film: str
    id_card_client: str | None
    data: date
    ora: float

    def __str__(self):
        id_c = self.id_card_client
        return f"Rezervare: ID rezervare: {self.id_entitate}, " \
               f"ID film: {self.id_film}, " \
               f"ID card client: {id_c if id_c is not None else '―'}, " \
               f"data rezervarii: {self.data.strftime('%d.%m.%Y')}, " \
               f"ora rezervarii: {format(self.ora, '.2f')}"
