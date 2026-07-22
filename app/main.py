from fastapi import FastAPI
app = FastAPI(
    title="GitHub Actions CI Demo",
    version="1.0"
)
@app.get("/")
def home():
    return {
        "message": "GitHub Actions CI Pipeline",
        "status": "Success"
    }
@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }