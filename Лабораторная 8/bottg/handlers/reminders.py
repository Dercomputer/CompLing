from aiogram import Router, F, types


router = Router()
reminders = []


@router.message(F.text.lower() == "список напоминаний")
async def list_remembers(message: types.Message):
    if not reminders:
        await message.answer("Напоминаний нет")
    else:
        output = ""
        for i in range(len(reminders)):
            output += ''.join(reminders[i]) + '\n'
        await message.answer(output)

# @router.message(F.text.lower() == "создать напоминание")
# async def create_reminder(message: types.Message):
#     await message.answer("Введите год на который хотите сделать напоминание")
#     year = message.text
#     await message.answer(f"{year}")
#
#     await message.answer("Введите месяц")
#     month = message.text
#     await message.answer("Введите день")
