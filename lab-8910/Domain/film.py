from dataclasses import dataclass
from Domain.entitate import Entitate


@dataclass
class Film(Entitate):
    """
    Descrie un film
    """
    titlu: str
    an_aparitie: str
    pret_bilet: float
    in_program: str

    def __str__(self):
        return f"Film: ID film: {self.id_entitate} , " \
               f"titlu: {self.titlu}, " \
               f"anul aparitiei: {self.an_aparitie}, " \
               f"pretul biletului: {self.pret_bilet}, " \
               f"in program(da/nu): {self.in_program}"
