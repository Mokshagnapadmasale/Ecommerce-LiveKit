import os 
import uvicorn 
from dotenv import load_dotenv
load_dotenv()

from uuid import uuid4
from fastapi import FastAPI,HTTPException
from livekit import api 
from livekit.api import LiveKitAPI,ListRoomsRequest
from fastapi.middleware.cors import CORSMiddleware
from livekit.api import VideoGrants,AccessToken
from starlette import status

LIVEKIT_API_KEY = os.getenv("LIVEKIT_API_KEY")
LIVEKIT_API_SECRET = os.getenv("LIVEKIT_API_SECRET")
LIVEKIT_URL = os.getenv("LIVEKIT_URL")

if not LIVEKIT_API_KEY or not LIVEKIT_API_SECRET:
    raise RuntimeError("LIVEKIT_API_KEY and LIVEKIT_API_SECRET must be set")


app = FastAPI(title='Ecommerce-livekit-token',description='This is server provider for livekit tokens')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/token",status_code=status.HTTP_200_OK)
def get_token(user_id: str):
    try:
        token = (
            api.AccessToken(LIVEKIT_API_KEY, LIVEKIT_API_SECRET)
            .with_identity(user_id)
            .with_grants(api.VideoGrants(room_join=True, room="ecommerce-room"))
            .to_jwt()
        )
        return {"token": token, "url": LIVEKIT_URL}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run("main:app",host="localhost",port=4000,reload=True)