from typing import Optional
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root() :
    return {"Hello" : "World"}

@app.get("/items/{item_id}")
def read_item(item_id : int, q : Optional[str] = None) :
    return {"item_id" : item_id, "q": q}

@app.get("/name/{name}")
def read_name(name : str, age : Optional[int] = None, school : Optional[str] = None) :
    return {"name" : name, "age" : f"{age}세", "school" : f"{school}학교"}

# @app.put("/items/{}")
# def put_item(item_name : str, is_offer : )

@app.get('/movie')
def get_moives(rank: Optional[int] = 10):
    import requests
    from bs4 import BeautifulSoup

    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    name = []
    for i in range(rank):
            name.append(soup.select(".title")[i].get_text().strip())

    return name

uvicorn.run(app, port=8000)