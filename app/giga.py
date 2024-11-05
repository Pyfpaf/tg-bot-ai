from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat
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
