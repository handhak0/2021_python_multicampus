# colab에서 실행

from fastapi import FastAPI
from typing import Optional
from fastapi.responses import HTMLResponse #text를 html코드로 인식시켜주기 위해
import nest_asyncio # colab에서 사용할 때, 남들이 볼 수 있는 api주소 생성
from pyngrok import ngrok
import uvicorn


app = FastAPI()


@app.get('/')
async def home():
    return 'Hello World'


@app.get('/movie', response_class=HTMLResponse)  # 응답 클래스를 지정해주면, return에서 텍스트를 html 코드로 인식
async def get_moives(rank: Optional[int] = 10):
    import requests
    from bs4 import BeautifulSoup

    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    name = []
    for i in range(rank):
        name.append(f'{i + 1}위 : {soup.select(".title")[i].get_text().strip()}')
    result = ''
    for i in name:
        result += f"<p>{i}\n"
    return result


ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, host='0.0.0.0', port=8000)