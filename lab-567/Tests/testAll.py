from Tests.testCRUD import test_adauga_obiect, test_get_by_ID, test_sterge_obiect, test_modifica_obiect
from Tests.testDomain import test_creeaza_obiect
from Tests.testFunctionalitati import test_concatenare_str, test_ordonare_cresc_dupa_pret, test_pret_max_fiecare_locatie, test_suma_fiecare_locatie, test_mutare_obiecte
from Tests.testUndoRedo import test_undo_redo


def run_all_tests():
    test_creeaza_obiect()
    test_adauga_obiect()
    test_get_by_ID()
    test_sterge_obiect()
    test_modifica_obiect()
    test_mutare_obiecte()
    test_concatenare_str()
    test_pret_max_fiecare_locatie()
    test_ordonare_cresc_dupa_pret()
    test_suma_fiecare_locatie()
    test_undo_redo()
