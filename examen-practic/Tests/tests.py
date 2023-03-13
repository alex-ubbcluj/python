from Domain.entity import Entity
from Repository.json_repository import JsonRepository
from Service.artist_service import ArtistService
from Tests.utils_tests import clear_file


def test_all():
    test_repository()
    test_adauga_artist()


def test_repository():
    clear_file("Tests/test-repository.json")
    repository = JsonRepository("Tests/test-repository.json")
    assert repository.read() == []
    entity_1 = Entity("1")
    repository.create(entity_1)
    assert repository.read() == [entity_1]
    entity_2 = Entity("2")
    repository.create(entity_2)
    assert repository.read() == [entity_1, entity_2]
    entity_3 = Entity("2")
    repository.update(entity_3)
    assert repository.read() == [entity_1, entity_3]
    repository.delete("1")
    assert repository.read() == [entity_3]


def test_adauga_artist():
    clear_file("Tests/test-artist.json")
    artist_repository = JsonRepository("Tests/test-artist.json")
    artist_service = ArtistService(artist_repository)
    artist_service.adauga("1", "nume", "categorie", 1324.34)
    artist_service.adauga("2", "nume2", "categorie2", 451324.34)
    assert len(artist_service.get_all()) == 2
