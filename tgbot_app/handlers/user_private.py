import logging
from aiogram import F, Router, types
from aiogram.filters import CommandStart
from aiogram.filters.logic import or_f
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from api.api_client import api_client
from filters.chat_types import ChatTypeFilter
from kb.reply_kb import START_KB

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(('private')))


class AddInfo(StatesGroup):
    text = State()


@user_private_router.message(or_f(CommandStart(), (F.text == '↩️ Назад')))
async def start(message: types.Message):
    hello_msg = 'Выбери, чем хочешь заняться🐶'
    if message.text == '/start':
        hello_msg = (f'Добро пожаловать, *{message.from_user.full_name}*!\n\n'
                     'Я тестовый *Бот*, ') + hello_msg

    await message.answer(
        hello_msg,
        reply_markup=START_KB,
    )

@user_private_router.message(F.text.lower() == 'добавить комментарий.')
async def create(message: types.Message,  state: FSMContext):
    await message.answer(
        'Введите информацию',
    )
    await state.set_state(AddInfo.text)
    

@user_private_router.message(AddInfo.text, F.text)
async def post_comment(
    message: types.Message,
    state: FSMContext,
):
    await state.set_data({
        'comment': message.text,
        'username': message.from_user.username
    })
    data = await state.get_data()
    await state.clear()
    logging.info(data)
    query = await api_client.post_query(
        url='https://my-nginx/api/comments-add/',
        prompt=data
    )
    response_text = 'Ошибка'
    if query:
        response_text = 'Успешно'
    await message.answer(response_text)


@user_private_router.message(F.text.lower() == 'зарегистрироваться.')
async def post_user(
    message: types.Message,
):
    data = {'username': message.from_user.username}
    query = await api_client.post_query(
        url='http://my-nginx/api/users-add/',
        prompt=data
    )
    response_text = 'Ошибка'
    if query:
        response_text = 'Успешно'
    await message.answer(response_text)


@user_private_router.message(
    F.text.lower() == 'посмотреть всех пользователей.'
)
async def get_users(
    message: types.Message,
):
    response = await api_client.get_query(
        url='http://my-nginx/api/users/',
    )
    text = ''
    for elem in response:
        text += f'{elem.get("id")}. *{elem.get("username")}*\n'
    if not text:
        text = 'Пусто'
    logging.info(text)
    await message.answer(text)


@user_private_router.message(F.text.lower() == 'посмотреть все комментарии.')
async def get_comments(
    message: types.Message,
):
    response = await api_client.get_query(
        url='http://my-nginx/api/comments/',
    )
    text = ''
    for elem in response:
        text += f'*{elem.get("username")}*:\n{elem.get("comment")}\n'
    logging.info(text)
    if not text:
        text = 'Пусто'
    await message.answer(text)
