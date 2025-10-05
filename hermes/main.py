from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def health_check():
    return {
        "message": "Mailr API v0.0.1",
        "status": "ok"
    }