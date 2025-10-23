
# Neon Postgres — Passo a passo (free)
1) Crie conta em https://neon.tech (free tier)
2) Crie um projeto → pegue a conexão (PSQL) e adapte ao async:
   - Sync: `postgresql://USER:PASSWORD@HOST/DB`
   - Async (usar no backend): `postgresql+asyncpg://USER:PASSWORD@HOST/DB`
3) No Render (backend) → Environment → adicione:
   - `DATABASE_URL=postgresql+asyncpg://USER:PASSWORD@HOST/DB`
4) Redeploy
5) Testes:
   - `POST /saturno/mock/load`
   - `GET /saturno/items`
