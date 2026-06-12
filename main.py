from fastapi import FastAPI

app = FastAPI(title="Piano Note Game API")

@app.get("/")
def read_root():
    """
    Route de base pour tester la connectivité (Healthcheck)
    """
    return {"status": "healthy", "message": "Bienvenue sur l'API Azure de Piano-Ops !"}
