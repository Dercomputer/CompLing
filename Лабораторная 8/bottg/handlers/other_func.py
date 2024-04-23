from aiogram import Router, F, types
from aiogram.filters import Command

router = Router()


@router.message(F.text.lower() == "помощь")
@router.message(Command("help"))
async def helper(message: types.Message):
    await message.reply(
        "Этот бот был создан для лабораторной работы номер 8 и имеет такой функционал: какие праздники есть в этот день"
        "(пока лишь памятные дни и дни воинской славы)")


@router.message(F.text.lower() == "нашли ошибку?")
async def correct(message: types.Message):
    await message.reply("Если обнаружили ошибку, столкнулись с багом - напишите сюда https://t.me/Der_Computer")


@router.message(F.text.lower() == "ы")
async def bab(message: types.Message):
    await message.reply("Проверка на ы пройдена - 1099")


@router.message(Command("dice"))
@router.message(F.text.lower() == "dice")
async def dice(message: types.Message):
    await message.answer_dice(emoji="🎲")


@router.message(Command("music"))
@router.message(F.text.lower() == "0")
async def zero(message: types.Message):
    await message.answer("0")
