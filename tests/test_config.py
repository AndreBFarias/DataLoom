"""Testes para src.core.config."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.core.config import ConfigManager


def test_get_default_config_tem_chaves_esperadas(tmp_path, monkeypatch):
    monkeypatch.setenv("HOME", str(tmp_path))
    cm = ConfigManager(app_name="DataLoomTest", config_file="test.json")
    default = cm._get_default_config()
    assert "gemini_api_key" in default
    assert "csv_separator" in default
    assert "dbt_project_path" in default
    assert "log_level" in default


def test_config_path_dentro_de_home_config(tmp_path, monkeypatch):
    monkeypatch.setenv("HOME", str(tmp_path))
    cm = ConfigManager(app_name="DataLoomTest", config_file="test.json")
    assert str(tmp_path) in str(cm.config_path)
    assert cm.config_path.endswith("test.json")


def test_load_config_cria_arquivo_padrao_se_nao_existir(tmp_path, monkeypatch):
    monkeypatch.setenv("HOME", str(tmp_path))
    cm = ConfigManager(app_name="DataLoomTest", config_file="test.json")
    assert Path(cm.config_path).exists()
    with open(cm.config_path) as f:
        data = json.load(f)
    assert data == cm._get_default_config()


def test_save_e_load_config_round_trip(tmp_path, monkeypatch):
    monkeypatch.setenv("HOME", str(tmp_path))
    cm = ConfigManager(app_name="DataLoomTest", config_file="test.json")
    cm.save_config({"gemini_api_key": "test_key", "log_level": "DEBUG"})
    cm2 = ConfigManager(app_name="DataLoomTest", config_file="test.json")
    assert cm2.config.get("gemini_api_key") == "test_key"
    assert cm2.config.get("log_level") == "DEBUG"
