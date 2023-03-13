from Domain.entitate import Entitate
from Domain.undo_redo_operation import UndoRedoOperation


class MultiApplyFunction(UndoRedoOperation):
    def __init__(self, function, value, obiecte_modificate: list[Entitate]):
        self.__function = function
        self.__value = value
        self.__opposite_value = -1 * value
        self.__obiecte_modificate = obiecte_modificate

    def do_undo(self):
        for entitate in self.__obiecte_modificate:
            self.__function(entitate, self.__opposite_value)

    def do_redo(self):
        for entitate in self.__obiecte_modificate:
            self.__function(entitate, self.__value)
