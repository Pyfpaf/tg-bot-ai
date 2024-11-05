from langchain_core.messages import HumanMessage
from langchain_community.chat_models import GigaChat
from config import GIGA_TOKEN


model = GigaChat(
    credentials=GIGA_TOKEN, 
    scope="GIGACHAT_API_PERS",
    # model="GigaChat-Pro",
    verify_ssl_certs=False
)


async def giga_text(request):
    response = model.invoke([HumanMessage(content=request)])
    return response.content
