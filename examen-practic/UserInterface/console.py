from Service.artist_service import ArtistService
from Service.concert_service import ConcertService


class Console:
    def __init__(self, artist_service: ArtistService, concert_service: ConcertService):
        self.artist_service = artist_service
        self.concert_service = concert_service

    def run_meniu(self):
        while True:
            print("1. Adauga artist")
            print("2. Adauga concert")
            print("3. Ordoneaza descrescator artistii dintr-o categorie dupa tarif")
            print("5. Export Json")
            print("a1. Afisate artisti")
            print("a2. Afisare concerte")
            print("x. Exit")
            optiune = input("Alegeti optiunea: ")
            if optiune == "1":
                self.adauga_artist()
            elif optiune == "2":
                self.adauga_concert()
            elif optiune == "3":
                self.ui_ordonare_categorie_dupa_tarif()
            elif optiune == "5":
                self.ui_export_json()
            elif optiune == "a1":
                self.afiseaza(self.artist_service.get_all())
            elif optiune == "a2":
                self.afiseaza(self.concert_service.get_all())
            elif optiune == "x":
                break
            else:
                print("Optiune invalida!")

    def afiseaza(self, entitati):
        for entitate in entitati:
            print(entitate)

    def adauga_artist(self):
        try:
            id_artist = input("Dati id-ul artistului: ")
            nume = input("Dati numele artistului: ")
            categorie = input("Dati categoria artistului: ")
            tarif = float(input("Dati tariful artistului: "))
            self.artist_service.adauga(id_artist, nume, categorie, tarif)
        except Exception as e:
            print(e)

    def adauga_concert(self):
        try:
            id_concert = input("Dati id-ul concertului: ")
            nume = input("Dati numele concertului: ")
            locatie = input("Dati locatia concertului: ")
            capacitate_locatie = int(input("Dati capacitatea locatiei: "))
            id_artist = input("Dati id-ul artistului: ")
            self.concert_service.adauga(id_concert, nume, locatie, capacitate_locatie, id_artist)
        except Exception as e:
            print(e)

    def ui_ordonare_categorie_dupa_tarif(self):
        try:
            categorie = input("Dati categoria: ")
            print(self.artist_service.ordonare_categorie_dupa_tarif(categorie))
        except Exception as e:
            print(e)

    def ui_export_json(self):
        try:
            filename = input("Dati numele fisierului in care se va face exportul: ")
            self.concert_service.export_json(filename)
        except Exception as e:
            print(e)
