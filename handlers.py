from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

import kb
import text

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)

@router.callback_query(F.data == "question")
async def answers(callback: types.CallbackQuery):
    await callback.message.answer(text.questions, reply_markup=kb.quiz)
    await callback.answer()

@router.callback_query(F.data == "q1")
async def ans1(callback: types.CallbackQuery):
    await callback.message.answer(text.q1)
    await callback.answer()

@router.callback_query(F.data == "q2")
async def ans2(callback: types.CallbackQuery):
    await callback.message.answer(text.q2)
    await callback.answer()

@router.callback_query(F.data == "q3")
async def ans3(callback: types.CallbackQuery):
    await callback.message.answer(text.q3)
    await callback.answer()

@router.callback_query(F.data == "q4")
async def ans4(callback: types.CallbackQuery):
    await callback.message.answer(text.q4)
    await callback.answer()

@router.callback_query(F.data == "q5")
async def ans5(callback: types.CallbackQuery):
    await callback.message.answer(text.q5)
    await callback.answer()

@router.callback_query(F.data == "q6")
async def ans6(callback: types.CallbackQuery):
    await callback.message.answer(text.q6)
    await callback.answer()

@router.callback_query(F.data == "pricelist")
async def pricelist(callback: types.CallbackQuery):
    await callback.message.answer(text.pricelist)
    await callback.answer()




