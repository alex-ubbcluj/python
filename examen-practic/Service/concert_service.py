import jsonpickle
from Domain.concert import Concert
from Repository.json_repository import JsonRepository


class ConcertService:
    def __init__(self, concert_repository: JsonRepository, artist_repository: JsonRepository):
        self.concert_repository = concert_repository
        self.artist_repository = artist_repository

    def get_all(self):
        return self.concert_repository.read()

    def adauga(self, id_concert: str, nume: str, locatie: str, capacitate_locatie: int, id_artist: str):
        """
        Adauga un concert in multimea de concerte
        :param id_concert: id-ul concertului
        :param nume: numele concertului
        :param locatie: locatia concertului
        :param capacitate_locatie: capacitatea locatiei
        :param id_artist: id-ul artistului
        :return:
        """
        if len(nume) == 0:
            raise ValueError("Numele concertului nu poate fi gol!")
        if self.artist_repository.read(id_artist) is None:
            raise ValueError("Artistul nu exista!")
        concert = Concert(id_concert, nume, locatie, capacitate_locatie, id_artist)
        self.concert_repository.create(concert)

    def export_json(self, filename):
        """
        Exporta toate locatiile tuturot artistilor, in format JSON
        :param filename: numele fisierului in care se va face exportul istoricului
        :return:
        """
        rezultat = {}
        for artist in self.artist_repository.read():
            locatii = []
            for concert in self.concert_repository.read():
                if artist.id_entity == concert.id_artist:
                    locatii.append(concert.locatie)
            rezultat[artist.nume] = locatii
        with open(filename, 'w') as f:
            f.write(jsonpickle.dumps(rezultat))
