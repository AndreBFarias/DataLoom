"""Testes para src.core.data."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.core.data import MUNICIPIOS_DATA


def test_municipios_e_lista_nao_vazia():
    assert isinstance(MUNICIPIOS_DATA, list)
    assert len(MUNICIPIOS_DATA) > 1000


def test_cada_municipio_tem_campos_obrigatorios():
    obrigatorios = {"id_municipio", "nome", "sigla_uf", "nome_uf"}
    for m in MUNICIPIOS_DATA[:10]:
        faltando = obrigatorios - set(m.keys())
        assert not faltando, f"Municipio {m.get('nome')} sem campos: {faltando}"


def test_ids_de_municipios_sao_unicos():
    ids = [m["id_municipio"] for m in MUNICIPIOS_DATA]
    assert len(ids) == len(set(ids)), "IDs de municipios nao sao unicos"
