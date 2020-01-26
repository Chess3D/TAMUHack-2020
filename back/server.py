from fastapi import FastAPI
import analysis

app = FastAPI()

@app.get("/")
async def root():
    analysis.update_speech()
    return analysis.get_wpm()