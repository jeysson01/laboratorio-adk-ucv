import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from agente_ucv.agent import explicar_concepto


def test_concepto_conocido():
    resultado = explicar_concepto("api")
    assert resultado["status"] == "success"
    assert "API" in resultado["explicacion"]

def test_concepto_desconocido():
    resultado = explicar_concepto("blockchain")
    assert resultado["status"] == "not_found"