import pytest
from app.service import saludar

def test_saludar():
    assert saludar("Clase 2") == "Hola, Clase 2!"