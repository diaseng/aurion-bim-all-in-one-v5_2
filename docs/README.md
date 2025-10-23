
# Aurion BIM Suite v5.2 — Monorepo (Render + Vercel + Neon Postgres + IFC.js + Metrics)
© 2025 Cleber Antonio Dias — Aurion BIM Suite v5.2. Todos os direitos reservados.

## Novidades v5.2
- IFC.js integrado no frontend (upload e visualização de arquivos .IFC)
- Neon Postgres pronto (SQLAlchemy async) + Alembic com migração inicial
- Rotas Saturno com persistência (CRUD básico de itens SINAPI mock)
- Métricas Prometheus em `/metrics` e HealthChecks `/health/ready` `/health/live`
- Dockerfile com `HEALTHCHECK` e entrypoint que roda migrations
