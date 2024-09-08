from typing import Annotated
from fastapi import APIRouter, Body
from pydantic import BaseModel
from controllers.exceptionHandlerController import ExceptionHandler
from services.chatService import LLMTask

chatRouter = APIRouter()
llmTask = LLMTask()
llmTask.modelLoad()

class Chat(BaseModel):
    question: str = ""
    answer: list[str] = []

@chatRouter.post('/getAnswer', response_model=Chat)
async def getAnswer(data: Annotated[Chat, Body]):
    try:
        result = llmTask.getHint(data.question)
        return {
            'question': data.question,
            'answer': result['answer']
        }
    except Exception as e:
        raise ExceptionHandler(status_code= 500, name= "Internal Server Error",  msg= str(e))