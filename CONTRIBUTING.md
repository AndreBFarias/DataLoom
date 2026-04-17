# Guia de Contribuição -- DataLoom

## Como Contribuir

1. Fork → branch feature → PR contra `main`
2. Commits em PT-BR (Conventional Commits)

## Padrão

- PT-BR com acentuação correta
- Zero emojis, zero menção IA
- Type hints sempre
- `logging` via `src/core/logger.py` (nunca print em produção)

## Configuração

```bash
python3 -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
```

## Testes

```bash
pytest tests/ -v
```

## Adicionar uma nova Tab

Crie em `src/tabs/nova_tab.py` herdando de `src/ui/base_tab.py`. Registre em `src/ui/app.py`.
