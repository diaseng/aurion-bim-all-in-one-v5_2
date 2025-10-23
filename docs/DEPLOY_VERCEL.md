
# Deploy detalhado — Vercel (frontend)
1) Importar repo do GitHub
2) Root: `apps/frontend`, Build: `npm ci && npm run build`, Output: `dist`
3) Env var: `VITE_API_URL=https://<seu-servico>.onrender.com`
4) GitHub Secrets: `VERCEL_TOKEN`, `VERCEL_ORG_ID`, `VERCEL_PROJECT_ID`
5) Push para `main` → workflow `vercel_frontend.yml` builda e deploya
