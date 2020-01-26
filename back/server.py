from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import analysis
import vision

app = FastAPI(
    title='Server to Server Comunication'
)

origins = [
    "null",
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/wpm")
async def root():
    analysis.update_speech()
    return int(analysis.get_wpm())

@app.get("/mood")
async def root():
    return int(vision.capture_image())