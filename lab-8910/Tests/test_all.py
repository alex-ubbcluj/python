from Tests.test_cautare_card_client_service import test_cautare_card_client
from Tests.test_cautare_film_service import test_cautare_film
from Tests.test_incrementare_puncte_interval_zile_service \
    import test_incrementare_puncte_interval_zile
from Tests.test_rezervari_interval_orar_service \
    import test_rezervari_interval_orar
from Tests.test_sterge_rez_interval_zile_service \
    import test_sterge_rez_interval_zile
from Tests.test_undo_redo import test_undo_redo


def test_all():
    test_cautare_film()
    test_cautare_card_client()
    test_rezervari_interval_orar()
    test_sterge_rez_interval_zile()
    test_incrementare_puncte_interval_zile()
    test_undo_redo()
