from fastapi import FastAPI
import analysis

app = FastAPI(
    title='Server to Server Comunication'
)

@app.get("/speed")
async def root():
    analysis.update_speech()
    return analysis.get_wpm()