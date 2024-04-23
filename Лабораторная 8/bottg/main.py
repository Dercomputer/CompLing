import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from handlers import buttons
from handlers import reminders
from handlers import other_func

bot = Bot(token="6642908478:AAHLmag8m__-Pz2BcKvy-shPVdYPQaZX2KQ")
dp = Dispatcher()
dp.include_router(buttons.router)
dp.include_router(reminders.router)
dp.include_router(other_func.router)


@dp.message(Command("start"))
@dp.message(F.text.lower() == "начать")
@dp.message(F.text.lower() == "старт")
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Помощь")],
        [types.KeyboardButton(text="Нашли ошибку?")],
        [types.KeyboardButton(text="Выбрать функцию")],
        [types.KeyboardButton(text="In progress...")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True)
    await message.answer("Привет, я бот напоминалка)))))", reply_markup=keyboard)


@dp.message(Command("menu"))
@dp.message(F.text.lower() == "выбрать функцию")
async def menu(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Праздники в выбранный день")],
        # [types.KeyboardButton(text="Создать напоминание")],
        [types.KeyboardButton(text="Список напоминаний")],
        [types.KeyboardButton(text="Вернуться назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True)
    await message.answer("Из предложенного списка выберите необходимое", reply_markup=keyboard)


@dp.message(F.text.lower() == "вернуться назад")
async def back(message: types.Message):
    await cmd_start(message)


@dp.message(Command("games"))
@dp.message(F.text.lower() == "in progress...")
async def testing(message: types.Message):
    kb = [
        [types.KeyboardButton(text="DICE")],
        [types.KeyboardButton(text="0")],
        [types.KeyboardButton(text="Вернуться назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True)
    await message.answer("описание не придумано", reply_markup=keyboard)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
