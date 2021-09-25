from fastapi import FastAPI, File, UploadFile
from typing import List
import os
import uvicorn

# import nest_asyncio
# from pyngrok import ngrok


app = FastAPI()



@app.get('/')
async def home() :
  return 'Hello World'

@app.post('/uploadfiles')
async def create_upload_files(files: List[UploadFile] = File(...)) :
  UPLOAD_DIRECTORY : "./"
  for file in files :
    contents = await file.read()
    with open(os.path.join(UPLOAD_DIRECTORY, file.filename), 'wb') as fp :
      fp.write(contents)
    print(file.filename)
  return {"filenames" : [file.filename for file in files]}

# ngrok_tunnel = ngrok.connect(8000)
# print('Public URL:', ngrok_tunnel.public_url)
# nest_asyncio.apply()
uvicorn.run(app, port = 8000)
