from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import logs

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173/"],  # Replace '*' with specific origins in production for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the logs router
app.include_router(logs.router)

@app.get("/")
def root():
    return {"message": "Welcome to the ROS Log Viewer Backend"}
