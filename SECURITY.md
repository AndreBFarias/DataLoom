# Política de Segurança -- DataLoom

## Versões Suportadas

| Versão | Suportada |
| ------ | --------- |
| 2.0.x  | sim       |

## Credenciais

A chave Gemini API é armazenada em `~/.config/DataLoom/config.json`. Nunca commite esse arquivo. O `.gitignore` exclui `venv/` e caches.

## Reportando

1. **Não** abra issue pública
2. Email ao mantenedor
3. Inclua descrição, passos, impacto

## Tempo de Resposta

- Recebimento: 48h
- Avaliação: 7 dias
- Correção: 30 dias

## Escopo

- `src/`
- Scripts de instalação
- CI/CD

## Fora do Escopo

- Vulnerabilidades em `pandas`, `customtkinter`, `matplotlib` (reporte upstream)
