from fastapi  import APIRouter
from pydantic import BaseModel, Field

from app.agent.chatbot import Chatbot


router = APIRouter(prefix="/chat", tags=["chat"])

chatbot = Chatbot()


class ChatRequest(BaseModel):
    conversation_id: str = Field(..., min_length=1)
    message: str = Field(..., min_length=1)


class ChatResponse(BaseModel):
    conversation_id: str
    answer: str


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = chatbot.answer(
        conversation_id=request.conversation_id,
        message=request.message,
    )

    return ChatResponse(
        conversation_id=request.conversation_id,
        answer=answer,
    )