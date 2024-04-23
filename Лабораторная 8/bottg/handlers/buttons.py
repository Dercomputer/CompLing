from aiogram import Router, F, types
from aiogram.utils.keyboard import InlineKeyboardBuilder


router = Router()


@router.message(F.text.lower() == "праздники в выбранный день")
async def holidays(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="01",
        callback_data="month1")
    )
    builder.add(types.InlineKeyboardButton(
        text="02",
        callback_data="month2")
    )
    builder.add(types.InlineKeyboardButton(
        text="03",
        callback_data="month3")
    )
    builder.add(types.InlineKeyboardButton(
        text="04",
        callback_data="month4")
    )
    builder.add(types.InlineKeyboardButton(
        text="05",
        callback_data="month5")
    )
    builder.add(types.InlineKeyboardButton(
        text="06",
        callback_data="month6")
    )
    builder.add(types.InlineKeyboardButton(
        text="07",
        callback_data="month7")
    )
    builder.add(types.InlineKeyboardButton(
        text="08",
        callback_data="month8")
    )
    builder.add(types.InlineKeyboardButton(
        text="09",
        callback_data="month9")
    )
    builder.add(types.InlineKeyboardButton(
        text="10",
        callback_data="month10")
    )
    builder.add(types.InlineKeyboardButton(
        text="11",
        callback_data="month11")
    )
    builder.add(types.InlineKeyboardButton(
        text="12",
        callback_data="month12")
    )
    builder.adjust(4)
    await message.answer("Выберите месяц", reply_markup=builder.as_markup())


@router.callback_query(F.data == "month1")
async def days_month1(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="25",
        callback_data="month1_25")
    )
    builder.add(types.InlineKeyboardButton(
        text="27",
        callback_data="month1_27")
    )
    await callback.message.answer("Выберите день", reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data == "month1_25")
async def give_holidays_month1_25(callback: types.CallbackQuery):
    await callback.message.answer("25 января - День российского студенчества")
    await callback.answer()


@router.callback_query(F.data == "month1_27")
async def give_holidays_month1_27(callback: types.CallbackQuery):
    await callback.message.answer("27 января - День полного освобождения Ленинграда от "
                                  "фашистской блокады (1944 год)")
    await callback.answer()


@router.callback_query(F.data == "month2")
async def days_month2(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="02",
        callback_data="month2_02")
    )
    builder.add(types.InlineKeyboardButton(
        text="15",
        callback_data="month2_15")
    )
    builder.add(types.InlineKeyboardButton(
        text="23",
        callback_data="month2_23")
    )
    await callback.message.answer("Выберите день", reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data == "month2_15")
async def give_holidays_month2_15(callback: types.CallbackQuery):
    await callback.message.answer("15 февраля - День памяти о россиянах, исполнявших служебный долг за пределами "
                                  "Отечества")
    await callback.answer()


@router.callback_query(F.data == "month2_02")
async def give_holidays_month2_02(callback: types.CallbackQuery):
    await callback.message.answer(
        "2 февраля - День разгрома советскими войсками немецко-фашистских войск в Сталинградской битве (1943 год)")
    await callback.answer()


@router.callback_query(F.data == "month2_23")
async def give_holidays_month2_23(callback: types.CallbackQuery):
    await callback.message.answer("23 февраля - День защитника Отечества")
    await callback.answer()


@router.callback_query(F.data == "month3")
async def days_month3(callback: types.CallbackQuery):
    await callback.message.answer("Нет памятных дат / дней воинской славы")
    await callback.answer()


@router.callback_query(F.data == "month4")
async def days_month4(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="12",
        callback_data="month4_12")
    )
    builder.add(types.InlineKeyboardButton(
        text="18",
        callback_data="month4_18")
    )
    builder.add(types.InlineKeyboardButton(
        text="19",
        callback_data="month4_19")
    )
    builder.add(types.InlineKeyboardButton(
        text="26",
        callback_data="month4_26")
    )
    builder.add(types.InlineKeyboardButton(
        text="27",
        callback_data="month4_27")
    )
    await callback.message.answer("Выберите день", reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data == "month4_12")
async def give_holidays_month4_12(callback: types.CallbackQuery):
    await callback.message.answer("12 апреля - День космонавтики")
    await callback.answer()


@router.callback_query(F.data == "month4_18")
async def give_holidays_month4_18(callback: types.CallbackQuery):
    await callback.message.answer("18 апреля - День победы русских воинов князя Александра Невского над немецкими "
                                  "рыцарями на Чудском озере (Ледовое побоище, 1242 год)")
    await callback.answer()


@router.callback_query(F.data == "month4_19")
async def give_holidays_month4_19(callback: types.CallbackQuery):
    await callback.message.answer("19 апреля - День принятия Крыма, Тамани и Кубани в состав Российской империи "
                                  "(1783 год)")
    await callback.answer()


@router.callback_query(F.data == "month4_26")
async def give_holidays_month4_26(callback: types.CallbackQuery):
    await callback.message.answer("26 апреля - День участников ликвидации последствий радиационных аварий и катастроф "
                                  "и памяти жертв этих аварий и катастроф")
    await callback.answer()


@router.callback_query(F.data == "month4_27")
async def give_holidays_month4_27(callback: types.CallbackQuery):
    await callback.message.answer("27 апреля - День российского парламентаризма")
    await callback.answer()


@router.callback_query(F.data == "month5")
async def days_month5(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="09",
        callback_data="month5_09")
    )
    builder.add(types.InlineKeyboardButton(
        text="12",
        callback_data="month5_12")
    )
    await callback.message.answer("Выберите день", reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data == "month5_09")
async def give_holidays_month5_09(callback: types.CallbackQuery):
    await callback.message.answer("9 мая - День Победы советского народа в Великой Отечественной войне 1941 - 1945 "
                                  "годов (1945 год)")
    await callback.answer()


@router.callback_query(F.data == "month5_12")
async def give_holidays_month5_12(callback: types.CallbackQuery):
    await callback.message.answer("12 мая - День победного завершения советскими войсками Крымской наступательной "
                                  "операции (1944 год)")
    await callback.answer()


@router.callback_query(F.data == "month6")
async def days_month6(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="22",
        callback_data="month6_22")
    )
    builder.add(types.InlineKeyboardButton(
        text="29",
        callback_data="month6_29")
    )
    await callback.message.answer("Выберите день", reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data == "month6_22")
async def give_holidays_month6_22(callback: types.CallbackQuery):
    await callback.message.answer("22 июня - День памяти и скорби - день начала Великой Отечественной войны (1941 год)")
    await callback.answer()


@router.callback_query(F.data == "month6_29")
async def give_holidays_month6_29(callback: types.CallbackQuery):
    await callback.message.answer("29 июня - День партизан и подпольщиков")
    await callback.answer()


@router.callback_query(F.data == "month7")
async def days_month7(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="07",
        callback_data="month7_07")
    )
    builder.add(types.InlineKeyboardButton(
        text="10",
        callback_data="month7_10")
    )
    builder.add(types.InlineKeyboardButton(
        text="28",
        callback_data="month7_28")
    )
    await callback.message.answer("Выберите день", reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data == "month7_07")
async def give_holidays_month7_07(callback: types.CallbackQuery):
    await callback.message.answer("7 июля - День победы русского флота над турецким флотом в Чесменском сражении "
                                  "(1770 год)")
    await callback.answer()


@router.callback_query(F.data == "month7_10")
async def give_holidays_month7_10(callback: types.CallbackQuery):
    await callback.message.answer("10 июля - День победы русской армии под командованием Петра Первого над шведами в "
                                  "Полтавском сражении (1709 год)")
    await callback.answer()


@router.callback_query(F.data == "month7_28")
async def give_holidays_month7_28(callback: types.CallbackQuery):
    await callback.message.answer("28 июля - День Крещения Руси")
    await callback.answer()


@router.callback_query(F.data == "month8")
async def days_month8(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="01",
        callback_data="month8_01")
    )
    builder.add(types.InlineKeyboardButton(
        text="09",
        callback_data="month8_09")
    )
    builder.add(types.InlineKeyboardButton(
        text="23",
        callback_data="month8_23")
    )
    await callback.message.answer("Выберите день", reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data == "month8_01")
async def give_holidays_month8_01(callback: types.CallbackQuery):
    await callback.message.answer("1 августа - День памяти российских воинов, погибших в Первой мировой войне "
                                  "1914 - 1918 годов")
    await callback.answer()


@router.callback_query(F.data == "month8_09")
async def give_holidays_month8_09(callback: types.CallbackQuery):
    await callback.message.answer("9 августа - День первой в российской истории морской победы русского флота под "
                                  "командованием Петра Первого над шведами у мыса Гангут (1714 год)")
    await callback.answer()


@router.callback_query(F.data == "month8_23")
async def give_holidays_month8_23(callback: types.CallbackQuery):
    await callback.message.answer("23 августа - День разгрома советскими войсками немецко-фашистских войск в "
                                  "Курской битве (1943 год)")
    await callback.answer()


@router.callback_query(F.data == "month9")
async def days_month9(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="03",
        callback_data="month9_03")
    )
    builder.add(types.InlineKeyboardButton(
        text="08",
        callback_data="month9_08")
    )
    builder.add(types.InlineKeyboardButton(
        text="11",
        callback_data="month9_11")
    )
    builder.add(types.InlineKeyboardButton(
        text="21",
        callback_data="month9_21")
    )
    builder.add(types.InlineKeyboardButton(
        text="30",
        callback_data="month9_30")
    )
    await callback.message.answer("Выберите день", reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data == "month9_03")
async def give_holidays_month9_03(callback: types.CallbackQuery):
    await callback.message.answer("3 сентября - День Победы над милитаристской Японией и окончания Второй мировой войны"
                                  " (1945 год). День солидарности в борьбе с терроризмом")
    await callback.answer()


@router.callback_query(F.data == "month9_11")
async def give_holidays_month9_11(callback: types.CallbackQuery):
    await callback.message.answer("11 сентября - День победы русской эскадры под командованием Ф.Ф. Ушакова над "
                                  "турецкой эскадрой у мыса Тендра (1790 год)")
    await callback.answer()


@router.callback_query(F.data == "month9_08")
async def give_holidays_month9_08(callback: types.CallbackQuery):
    await callback.message.answer("8 сентября - День Бородинского сражения русской армии под командованием М.И. "
                                  "Кутузова с французской армией (1812 год)")
    await callback.answer()


@router.callback_query(F.data == "month9_21")
async def give_holidays_month9_21(callback: types.CallbackQuery):
    await callback.message.answer("21 сентября - День победы русских полков во главе с великим князем Дмитрием Донским "
                                  "над монголо-татарскими войсками в Куликовской битве (1380 год)")
    await callback.answer()


@router.callback_query(F.data == "month9_30")
async def give_holidays_month9_30(callback: types.CallbackQuery):
    await callback.message.answer("30 сентября - День воссоединения Донецкой Народной Республики, Луганской Народной "
                                  "Республики, Запорожской области и Херсонской области с Российской Федерацией "
                                  "(2022 год)")
    await callback.answer()


@router.callback_query(F.data == "month10")
async def days_month10(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="09",
        callback_data="month10_09")
    )
    await callback.message.answer("Выберите день", reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data == "month10_09")
async def give_holidays_month10_09(callback: types.CallbackQuery):
    await callback.message.answer("9 октября - День разгрома советскими войсками немецко-фашистских войск в битве "
                                  "за Кавказ (1943 год)")
    await callback.answer()


@router.callback_query(F.data == "month11")
async def days_month11(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="04",
        callback_data="month11_04")
    )
    builder.add(types.InlineKeyboardButton(
        text="07",
        callback_data="month11_07")
    )
    builder.add(types.InlineKeyboardButton(
        text="21",
        callback_data="month11_21")
    )
    await callback.message.answer("Выберите день", reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data == "month11_04")
async def give_holidays_month11_04(callback: types.CallbackQuery):
    await callback.message.answer("4 ноября - День народного единства")
    await callback.answer()


@router.callback_query(F.data == "month11_07")
async def give_holidays_month11_07(callback: types.CallbackQuery):
    await callback.message.answer("7 ноября - День Октябрьской революции 1917 года. День проведения военного парада на "
                                  "Красной площади в городе Москве в ознаменование двадцать четвертой годовщины Великой"
                                  " Октябрьской социалистической революции (1941 год) ")
    await callback.answer()


@router.callback_query(F.data == "month11_21")
async def give_holidays_month11_21(callback: types.CallbackQuery):
    await callback.message.answer("21 ноября - День Военной присяги")
    await callback.answer()


@router.callback_query(F.data == "month12")
async def days_month12(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="01",
        callback_data="month12_01")
    )
    builder.add(types.InlineKeyboardButton(
        text="03",
        callback_data="month12_03")
    )
    builder.add(types.InlineKeyboardButton(
        text="05",
        callback_data="month12_05")
    )
    builder.add(types.InlineKeyboardButton(
        text="09",
        callback_data="month12_09")
    )
    builder.add(types.InlineKeyboardButton(
        text="12",
        callback_data="month12_12")
    )
    builder.add(types.InlineKeyboardButton(
        text="24",
        callback_data="month12_24")
    )
    builder.adjust(3)
    await callback.message.answer("Выберите день", reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data == "month12_01")
async def give_holidays_month12_01(callback: types.CallbackQuery):
    await callback.message.answer("1 декабря - День победы русской эскадры под командованием П.С. Нахимова над турецкой"
                                  " эскадрой у мыса Синоп (1853 год)")
    await callback.answer()


@router.callback_query(F.data == "month12_05")
async def give_holidays_month12_05(callback: types.CallbackQuery):
    await callback.message.answer("5 декабря - День начала контрнаступления советских войск против немецко-фашистских "
                                  "войск в битве под Москвой (1941 год)")
    await callback.answer()


@router.callback_query(F.data == "month12_24")
async def give_holidays_month12_24(callback: types.CallbackQuery):
    await callback.message.answer("24 декабря - День взятия турецкой крепости Измаил русскими войсками под "
                                  "командованием А.В. Суворова (1790 год)")
    await callback.answer()


@router.callback_query(F.data == "month12_09")
async def give_holidays_month12_09(callback: types.CallbackQuery):
    await callback.message.answer("9 декабря - День Героев Отечества")
    await callback.answer()


@router.callback_query(F.data == "month12_03")
async def give_holidays_month12_03(callback: types.CallbackQuery):
    await callback.message.answer("3 декабря - День Неизвестного Солдата")
    await callback.answer()


@router.callback_query(F.data == "month12_12")
async def give_holidays_month12_12(callback: types.CallbackQuery):
    await callback.message.answer("12 декабря - День Конституции Российской Федерации")
    await callback.answer()
