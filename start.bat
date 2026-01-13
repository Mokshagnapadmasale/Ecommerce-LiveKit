@echo off
echo Starting LiveKit E-Commerce Voicebot...

start cmd /k "cd app\backend && python main.py"
start cmd /k "cd app\backend\tools && python ecommerce_server.py"
start cmd /k "cd app\backend && python agent.py dev"
start cmd /k "cd app\frontend && pnpm run dev"

echo All services launched.