from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from app.openai import gpt_text
from app.giga import giga_text

import app.keyboards as kb
from app.states import Chatai, Chatgiga

user = Router()


@user.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать!', reply_markup=kb.main)


@user.message(F.text == 'OpenAI')
async def openai_chat(message: Message, state: FSMContext):
    await state.set_state(Chatai.text)
    await message.answer('Введите Ваш запрос')


@user.message(Chatai.text)
async def chatai_resp(message: Message, state: FSMContext):
    await state.set_state(Chatai.wait)
    # response = await gpt_text(message.text, 'gpt-3.5-turbo')
    # await message.answer(response)
    await message.answer(message.text)
    await message.answer('Данная модель отключена в учебных целях')
    await state.clear()


@user.message(Chatai.wait)
async def chatai_wait(message: Message):
    await message.answer('Подождите, сообщение генерируется')


@user.message(F.text == 'GigaChat')
async def giga_chat(message: Message, state: FSMContext):
    await state.set_state(Chatgiga.text)
    await message.answer('Введите Ваш запрос')


@user.message(Chatgiga.text)
async def chatgiga_resp(message: Message, state: FSMContext):
    await state.set_state(Chatgiga.wait)
    response = await giga_text(message.text)
    await message.answer(response)
    await state.clear()


@user.message(Chatgiga.wait)
async def chatgiga_wait(message: Message):
    await message.answer('Подождите, сообщение генерируется')