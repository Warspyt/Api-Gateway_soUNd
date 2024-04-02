from fastapi import FastAPI, File, UploadFile, HTTPException, APIRouter
from fastapi.responses import StreamingResponse, JSONResponse
import requests

app_streaming = APIRouter()


@app_streaming.get("/")
async def upload_song():
    return "Funciona la api"


@app_streaming.post("/upload")
async def upload_song(file: UploadFile):
    try:
        upload_url = "http://localhost:3001/audio/upload"
        files = {"audio": (file.filename, file.file, file.content_type)}
        response = requests.post(upload_url, files=files)
        response_data = response.json()

        return response_data
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al subir la canción: {str(e)}")


@app_streaming.get("/play/{song_id}")
async def play_song(song_id: str):
    try:
        stream_url = f"http://localhost:3001/audio/streaming/{song_id}"
        response = requests.get(stream_url, stream=True)
        if response.status_code == 200:
            return StreamingResponse(response.iter_content(chunk_size=10000), media_type="audio/mp3")
        else:
            raise HTTPException(status_code=response.status_code,
                                detail="No se pudo reproducir la canción")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al reproducir la canción: {str(e)}")


@app_streaming.get("/canciones")
async def canciones():
    try:
        stream_url = "http://localhost:3001/audio"
        response = requests.get(stream_url)
        if response.status_code == 200:
            data = response.json()
            return JSONResponse(content=data)
        else:
            raise HTTPException(status_code=response.status_code,
                                detail="No se pudieron encontrar las canciones")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al encontrar las canciones: {str(e)}")
