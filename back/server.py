from fastapi import FastAPI
import analysis

app = FastAPI(
    title='Server to Server Comunication'
)

@app.get("/wpm")
async def root():
    analysis.update_speech()
    return analysis.get_wpm()