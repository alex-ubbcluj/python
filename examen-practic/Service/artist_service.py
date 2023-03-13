from Domain.artist import Artist
from Repository.json_repository import JsonRepository


class ArtistService:
    def __init__(self, artist_repository: JsonRepository):
        self.artist_repository = artist_repository

    def get_all(self):
        return self.artist_repository.read()

    def adauga(self, id_artist: str, nume: str, categorie: str, tarif: float):
        """
        Adauga un artist in multimea de artisti
        :param id_artist: id-ul artistului
        :param nume: numele artistului
        :param categorie: categoria artistului
        :param tarif: tariful artistului
        :return:
        """
        if len(nume) == 0:
            raise ValueError("Numele artistului nu poate fi gol!")
        artist = Artist(id_artist, nume, categorie, tarif)
        self.artist_repository.create(artist)

    def ordonare_categorie_dupa_tarif(self, categorie):
        """
        Ordoneaza descrescator artistii dintr-o categorie dupa tarif
        :param categorie: categoria
        :return: artistii ordonati descrescator
        """
        rezultat = []
        for artist in self.artist_repository.read():
            if artist.categorie == categorie:
                rezultat.append(artist)
        return sorted(rezultat, key=lambda x: x.tarif, reverse=True)
