from Repository.json_repository import JsonRepository
from Service.artist_service import ArtistService
from Service.concert_service import ConcertService
from Tests.tests import test_all
from UserInterface.console import Console


def main():
    artist_repository = JsonRepository("artisti.json")
    artist_service = ArtistService(artist_repository)
    concert_repository = JsonRepository("concerte.json")
    concert_service = ConcertService(concert_repository, artist_repository)
    console = Console(artist_service, concert_service)
    console.run_meniu()


if __name__ == '__main__':
    test_all()
    main()
