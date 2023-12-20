from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    '*',
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
class StockRequest(BaseModel):
    symbol: str

@app.get("/")
async def root():
    return {"message": "FastAPI Service is running"}

@app.post("/get_stock")
async def get_stock(data: StockRequest):
    # Here you might fetch real stock data, for simplicity returning a static response
    return {"symbol": data.symbol, "price": 100.0}


