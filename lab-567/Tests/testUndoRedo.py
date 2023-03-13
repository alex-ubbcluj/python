from Logic.CRUD import adauga_obiect


def test_undo_redo():
    test_list = []
    undo_list = []
    redo_list = []

    #adaugam un obiect
    undo_list.append(test_list)
    redo_list.clear()
    test_list = adauga_obiect(33, "Frigider Samsung", "Clasa energetica A+, volum 384L", 1949.0, "C004", test_list)

    #adaugam inca un obiect
    undo_list.append(test_list)
    redo_list.clear()
    test_list = adauga_obiect(256, "Monitor Dell", "23.8'', Full HD, 144Hz", 1099.0, "C503", test_list)

    #adaugam inca un obiect
    undo_list.append(test_list)
    redo_list.clear()
    test_list = adauga_obiect(1, "obiect test 1", "descriere 1", 4000.0, "LOC1", test_list)

    #undo scoate ultimul obiect adaugat
    if len(undo_list) > 0:
        redo_list.append(test_list)
        test_list = undo_list.pop()
    assert len(test_list) == 2

    #inca un undo scoate penultimul obiect adaugat
    if len(undo_list) > 0:
        redo_list.append(test_list)
        test_list = undo_list.pop()
    assert len(test_list) == 1

    # inca un undo scoate penultimul obiect adaugat
    if len(undo_list) > 0:
        redo_list.append(test_list)
        test_list = undo_list.pop()
    assert len(test_list) == 0

    #inca un undo nu face nimic
    if len(undo_list) > 0:
        redo_list.append(test_list)
        test_list = undo_list.pop()
    assert len(test_list) == 0

    #adaugam trei obiecte
    undo_list.append(test_list)
    redo_list.clear()
    test_list = adauga_obiect(1, "obiect test 1", "descriere 1", 4000.0, "LOC1", test_list)
    undo_list.append(test_list)
    redo_list.clear()
    test_list = adauga_obiect(2, "obiect test 2", "descriere 2", 1000.0, "LOC2", test_list)
    undo_list.append(test_list)
    redo_list.clear()
    test_list = adauga_obiect(3, "obiect test 3", "descriere 3", 3000.0, "LOC2", test_list)

    #redo nu face nimic
    if len(redo_list) > 0:
        undo_list.append(test_list)
        test_list = redo_list.pop()
    assert len(test_list) == 3

    #doua undo-uri scot ultimele 2 obiecte
    if len(undo_list) > 0:
        redo_list.append(test_list)
        test_list = undo_list.pop()
    if len(undo_list) > 0:
        redo_list.append(test_list)
        test_list = undo_list.pop()
    assert len(test_list) == 1

    #redo anuleaza ultimul undo, daca ultima operatie e undo
    if len(redo_list) > 0:
        undo_list.append(test_list)
        test_list = redo_list.pop()
    assert len(test_list) == 2

    #redo anuleaza si primul undo
    if len(redo_list) > 0:
        undo_list.append(test_list)
        test_list = redo_list.pop()
    assert len(test_list) == 3

    #doua undo-uri scot ultimele 2 obiecte
    if len(undo_list) > 0:
        redo_list.append(test_list)
        test_list = undo_list.pop()
    if len(undo_list) > 0:
        redo_list.append(test_list)
        test_list = undo_list.pop()
    assert len(test_list) == 1

    #adaugam un obiect
    undo_list.append(test_list)
    redo_list.clear()
    test_list = adauga_obiect(4, "obiect test 4", "descriere 4", 2000.0, "LOC1", test_list)

    #redo nu face nimic, deoarece ultima operatie nu este un undo
    if len(redo_list) > 0:
        undo_list.append(test_list)
        test_list = redo_list.pop()
    assert len(test_list) == 2

    #undo anuleaza adaugarea lui o4
    if len(undo_list) > 0:
        redo_list.append(test_list)
        test_list = undo_list.pop()
    assert len(test_list) == 1

    #undo anuleaza adaugarea lui o1 - practic se continua sirul de undo de la pct 14
    if len(undo_list) > 0:
        redo_list.append(test_list)
        test_list = undo_list.pop()
    assert len(test_list) == 0

    #se anuleaza ultimele 2 undo-uri
    if len(redo_list) > 0:
        undo_list.append(test_list)
        test_list = redo_list.pop()
    if len(redo_list) > 0:
        undo_list.append(test_list)
        test_list = redo_list.pop()
    assert len(test_list) == 2

    #redo nu face nimic
    if len(redo_list) > 0:
        undo_list.append(test_list)
        test_list = redo_list.pop()
    assert len(test_list) == 2
