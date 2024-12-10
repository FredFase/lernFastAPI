from fastapi import FastAPI,Query
from typing import Optional
from datetime import date

app = FastAPI()

@app.get('/hotels')
def root(hotel_id: int,
          location: str,
          date_from: date, 
          date_to: date,
          spa: Optional[bool] = None,
          stars:Optional[int] = Query(None, ge=1, le=5),
          
        ):
    return hotel_id, date_from, date_to
