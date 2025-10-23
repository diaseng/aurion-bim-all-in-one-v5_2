Write-Host '== Aurion BIM v5.2 :: Dev local =='
cd ../apps/backend
python -m venv .venv
./.venv/Scripts/Activate.ps1
pip install -r requirements.txt
$env:DATABASE_URL=''
Start-Process powershell -ArgumentList '-NoExit','-Command','cd ../apps/backend; . ./.venv/Scripts/Activate.ps1; uvicorn app.main:app --host 0.0.0.0 --port 8000'
cd ../../apps/frontend
npm i
npm run dev
