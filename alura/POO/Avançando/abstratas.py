from abc import ABC # abstract base classes
from collections.abc import MutableSequence
from numbers import Complex


class Numero(Complex):
    pass


class Playlist(MutableSequence):
    pass


filmes = Playlist()
numero = Numero()
