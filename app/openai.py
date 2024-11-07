from openai import AsyncOpenAI
import httpx
from config import AITOKEN

client = AsyncOpenAI(
    api_key=AITOKEN,
    http_client=httpx.AsyncClient(
        proxies='http://login:pswrd@77.98.18.107:6485',
        transport=httpx.HTTPTransport(local_address='0.0.0.0')))


async def gpt_text(req, model):
    completion = await client.chat.completions.create(
        messages=[{'role': 'user', 'content': req}],
        model=model
    )
    return completion.choices[0].message.content