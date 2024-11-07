from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo
from aiogram.filters import Command
from bot_token import token
import asyncio

bot = Bot(token=token)
dp = Dispatcher()

@dp.message(Command("start"))
async def info(message: types.Message):
    name = message.from_user.first_name
    surname = message.from_user.last_name
    initials = f"{name} {surname}" if surname else name
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Основная информация"),KeyboardButton(text="Забронировать номер")],
            [KeyboardButton(text="Обратиться к администратору отеля")]
        ],
        resize_keyboard=True
    )
    await message.answer(f"Доброго времени суток, {initials}!", reply_markup=keyboard)

@dp.message(Command("info"))
async def InfoHandler(message: types.Message):
    await message.answer("<b>Что можно сказать о нашем отеле? Давай я тебе поведаю 🦾</b>\n", parse_mode='HTML')
    await message.answer('Отель "Дюны Золотые" категории 4* (звезды) работает по системе « Все включено», включает в себя 8 коттеджей и 3 корпуса с номерным фондом 116 номеров от "Стандарта" до "Семейных апартаментов".')
    await message.answer( '«Дюны Золотые» — это отличное место, чтобы отдохнуть всей семьей или в кругу друзей, провести корпоративный праздник, а также остановиться здесь, если вы прилетели в командировку. Только в летний сезон отель принимает более 4500 гостей.')
    await message.answer('- Общая площадь: 2,2 га закрытой территории\n- Ресторан "шведской линии" «Le Dune»\n- Бар «Acapulco» с уютной террасой\n- Собственный песчаный пляж: 3 500 м²\n- Пляжная зона со всеми удобствами\n- Пляжный бар «Tamarix»\n- Детский парк развлечений «DюноLэнд» и мини-клуб\n- SPA комплекс\n- Подогреваемый бассейн "Лагуна" — 108 м²\n- Множество уголков для уединения\n- Чудесный ландшафт и вид на бескрайнее море')
    await message.answer('Лето — пора отпусков, пляжного отдыха и морских развлечений. Июнь можно охарактеризовать любимым месяцем для тех, кто не привык к сильному зною: днем температура воздуха поднимается до +25…+28, а ночью не опускается ниже +18…+20, вода также постепенно, но уверенно прогревается и становится подходящей для купания ближе к середине месяца. Июль и август — наиболее знойные месяцы в Анапе, нередко в это время столбики термометров показывают +35…+40 в дневное время. Зато температура воды в это время действительно идеальная для всех — и для взрослых, и для детишек, она колеблется в пределах +24…+27. Отсутствие дождей, теплый, даже жаркий воздух и немного охлаждающий его морской бриз — именно так можно охарактеризовать климат летней Анапы.')

@dp.message(lambda message: message.text.lower() == "основная информация")
async def InfoHandler(message: types.Message):
    await message.answer('🖥️ Сайт "Золотые Дюны" - https://clck.ru/39QvtG\n\n📎 Телеграм канал - https://clck.ru/39QvuP\n\n📱 Страница Вконтакте - https://clck.ru/39TGpE\n\n🏖️ Курортный сбор - https://clck.ru/39S4TB\n\n📍 Адрес - г.Анапа, Джемете, Пионерский проспект 223\n\n🧭 Гугл карты - https://clck.ru/39RkrK\n\n🧭 Яндекс карты - https://clck.ru/39RmPs')

@dp.message(lambda message: message.text.lower() == "забронировать номер")
async def TakeHotel(message: types.Message):
    await message.answer('❓ Чтобы ознакомиться с ценовой политикой нашего отеля, используйте команду /price\n(напишите или просто нажмите на неё)\n\n❗️ Также как и в других отелях, у нас присутствует [курортный сбор](https://clck.ru/39S4TB), с ним можно ознакомиться, нажав главную кнопку снизу "Основная информация", или нажать на само слово\n\n✔️ Для бронирования номера, нажмите главную кнопку снизу "Обратиться к администратору отеля"', parse_mode='Markdown')

@dp.message(lambda message: message.text.lower() == "обратиться к администратору отеля")
async def TalkWithADM(message: types.Message):
    await message.answer('💻 Телеграм диалог - https://clck.ru/39Rn4T\n\n☎ Номер - +7-958-497-0515\n\n☎ Номер - +8-800-505-8552\n\n📧 Электронная почта - sales@dunesgold.ru')

@dp.message(Command("price"))
async def HotelPrice(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Нажмите на меня, для создания нового окна",web_app=WebAppInfo(url="https://dunesgold.ru/tabron#popup:inf"))]
        ]
    )
    await message.answer("Окончательная цена номера зависит от многих факторов ❗️\nНе стоит и забывать, что у нас присутствует [курортный сбор](https://clck.ru/39S4TB)", reply_markup=keyboard, parse_mode='Markdown')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        print(".: Launched")
        asyncio.run(main())
    except KeyboardInterrupt:
        print(".: Stopped")