
# Deploy detalhado — Render (backend)
1) Criar serviço Web (Render) com Root Dir `apps/backend` e Runtime **Docker**
2) Variáveis:
   - `ENVIRONMENT=production`
   - `PORT=10000`
   - (opcional) `DATABASE_URL=postgresql+asyncpg://<user>:<pass>@<host>/<db>`
3) API Key + Service ID → GitHub Secrets: `RENDER_API_KEY`, `RENDER_SERVICE_ID`
4) Push para `main` → workflow `render_backend.yml` deploya
5) Testes: `/health/ping`, `/health/ready`, `/metrics`, `/saturno/mock/load`, `/saturno/items`
