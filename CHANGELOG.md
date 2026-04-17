# Changelog

## [2.0.0] - 2026-04-16

### Mudado
- Projeto renomeado de `Python-Data-Toolkit` para `DataLoom` (sprint S15 do portfólio)
- `pyproject.toml` corrigido: nome `dataloom`, build-backend `setuptools.build_meta`, URL do repo atualizada
- Removido `README.md.final` duplicata

### Adicionado
- `tests/test_config.py` (4 testes para ConfigManager)
- `tests/test_data.py` (3 testes para MUNICIPIOS_DATA)
- `.github/workflows/ci.yml`
- `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `SECURITY.md`, `.mailmap`

## [1.0.0] - 2026-03-16

### Adicionado
- Interface gráfica com CustomTkinter para manipulação de dados
- 11 módulos GUI: Limpador, Visualizador, Profiler, Comparador, Unificador, ETL Preparer, Segmenter, Auxiliador (IA Gemini), Extrator, Geolocalizador, Anonymizer
- Settings tab com ConfigManager persistente
- Scripts de instalação para Linux
