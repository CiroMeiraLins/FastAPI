from fastapi import FastAPI

app = FastAPI()


@app.get("/NSU/{nsu}")
async def read_item(nsu: int):
    
    return {"nsu": nsu}