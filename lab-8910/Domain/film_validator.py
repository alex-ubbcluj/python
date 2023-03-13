from Domain.film import Film
from Domain.film_error import FilmError


class FilmValidator:
    def validate(self, film: Film):
        erori = []
        if film.pret_bilet < 0:
            erori.append("Pretul trebuie sa fie pozitiv!")
        if film.in_program not in ["da", "nu"]:
            erori.append("'in program' poate fi doar 'da' sau 'nu'")
        if len(erori) > 0:
            raise FilmError(erori)
