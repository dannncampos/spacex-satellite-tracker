echo "Waiting for MySql"
sleep 1m
echo "Starting FastAPI"
uvicorn main:app --host 0.0.0.0 --reload --port 8000