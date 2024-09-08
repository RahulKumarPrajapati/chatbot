from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.chatController import chatRouter

app = FastAPI()

# Define the origins that are allowed to make requests to this API.
origins = [
    '*'
]

# Add CORSMiddleware to the FastAPI application.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # List of allowed methods (e.g., GET, POST). "*" allows all methods.
    allow_headers=["*"],  # List of allowed headers. "*" allows all headers.
)

app.include_router(chatRouter, prefix="/api/chat")

@app.get("/")
async def read_root():
    return {"message": "Hello ChatBot!"}