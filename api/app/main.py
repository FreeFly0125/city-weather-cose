from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from app.api.routes.routes import api_router

app = FastAPI()
app.include_router(api_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def good_luck():
    return {
        "Good": "Luck!",
    }


@app.get(path="/health", status_code=200)
def checkServerHealth():
    return {"status": "Hello, World"}


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )
