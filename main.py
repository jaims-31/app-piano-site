from fastapi import FastAPI

app = FastAPI(title="Piano Note Game API")


@app.get("/")
def read_root():
    """
    Route de base pour tester la connectivité (Healthcheck)
    """
    return {"status": "healthy", "message": "Bienvenue sur l'API Azure de Piano-Ops !"}

from fastapi import FastAPI
from typing import List
import random

app = FastAPI(title="Piano Note Game API")

# positions des notes
SOL_NOTES_POSITIONS = {
    "DO_G2": 94.25, "RÉ_G2": 87.0, "MI_G": 79.75, "FA_G": 72.5, "SOL_G": 65.25, "LA_G": 58.0, "SI_G": 50.75,
    "DO": 43.5, "RÉ": 36.25, "MI": 29.0, "FA": 21.75, "SOL": 14.5, "LA": 7.25, "SI": 0,
    "DO_A": -7.25, "RÉ_A": -14.5, "MI_A": -21.75, "FA_A": -29.0, "SOL_A": -36.25, "LA_A": -43.5, "SI_A": -50.75,
    "DO_A2": -58.0, "RÉ_A2": -65.25, "MI_A2": -72.5, "FA_A2": -79.75, "SOL_A2": -87.0
}

FA_NOTES_POSITIONS = {
    "DO_G3": 108.75, "RÉ_G3": 101.5, "MI_G2": 94.25, "FA_G2": 87.0, "SOL_G2": 79.75, "LA_G2": 72.5, "SI_G2": 65.25,
    "DO_G2": 58.0, "RÉ_G2": 50.75, "MI_G": 43.5, "FA_G": 36.25, "SOL_G": 29.0, "LA_G": 21.75, "SI_G": 14.5,
    "DO": 7.25, "RÉ": 0, "MI": -7.25, "FA": -14.5, "SOL": -21.75, "LA": -29.0, "SI": -36.25,
    "DO_A": -43.5, "RÉ_A": -50.75, "MI_A": -58.0, "FA_A": -65.25, "SOL_A": -72.5, "LA_A": -79.75, "SI_A": -87.0
}

@app.get("/")
def read_root():
    return {"status": "healthy", "message": "Bienvenue sur l'API Azure de Piano-Ops !"}