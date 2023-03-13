from typing import Protocol
from Domain.entitate import Entitate


class Repository(Protocol):
    def read(self, id_entitate=None):
        ...

    def add(self, entitate: Entitate):
        ...

    def delete(self, id_entitate):
        ...

    def update(self, entitate: Entitate):
        ...
