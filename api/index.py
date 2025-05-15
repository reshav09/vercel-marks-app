from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import List
import json
import os

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks from JSON file
json_path = os.path.join(os.path.dirname(__file__), "vercel-data.json") 
with open(json_path, "r") as f:
    data = json.load(f)

# Build a dictionary for fast lookup
marks_db = {entry["name"]: entry["marks"] for entry in data}

@app.get("/api")
async def get_marks(name: List[str] = []):
    result = [marks_db.get(n, 0) for n in name]
    return JSONResponse(content={"marks": result})

