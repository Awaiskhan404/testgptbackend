from fastapi import FastAPI
from app.routers import health, chat
from mangum import Mangum

app = FastAPI()

# Include routers
app.include_router(health.router)
app.include_router(chat.router)


handler = Mangum(app)

# Start point for the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)