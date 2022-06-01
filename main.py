import logging
import re
import time

from keyboards import *
import aiocron
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import ChatNotFound
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

from database import Sql

storage = MemoryStorage()
bot = Bot(token="TOKEN BOT")
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)
db = Sql('database.db')


class FSMail_user(StatesGroup):
    sms = State()


class FSMail_send_user(StatesGroup):
    sms_user = State()


@dp.message_handler(commands="start")
async def cmd_test1(message: types.Message):
    admin = 'id admin'
    if message.from_user.id == admin:
        await message.answer('Привет', reply_markup=admin_key)
    else:
        await message.answer('Рада, что Вы подписались на '
                             'мои '
                             'уведомления. В '
                             'этотого бота'
                             ' можно написать любой вопрос, и мы на него ответим '
                             'в самое ближайшее время', reply_markup=key)
        if not db.subscriber_exists(message.from_user.id):
            db.add_subscriber(message.from_user.id)


@dp.message_handler(content_types='text')
async def button(message: types.Message):
    if message.text == 'Задать вопрос':
        if not db.message_exists(message.from_user.id):
            await message.answer('Напишите Ваше сообщение:', reply_markup=types.ReplyKeyboardRemove())
            await bot.delete_message(message.from_user.id, message.message_id)
            await FSMail_user.sms.set()
        else:
            await message.answer('Вы уже отправили одно сообщение, ждите ответа!')
    elif message.text == 'Входящие сообщения':
        global id_sub
        try:
            for k in db.push_msg():
                id_sub = k[0]
        except ChatNotFound:
            pass
        if db.check():
            try:
                time.sleep(0.1)
                await bot.send_message(message.from_user.id, k[1], reply_markup=ok)
            except (UnboundLocalError, ChatNotFound):
                pass
        else:
            await message.answer('Сообщений нет')
    elif message.text == 'Статистика':
        len_user = db.lenuser()
        a = do_work(len_user)
        okk = db.true()
        b = (re.sub(r"[',()/\]\[]", '', str(okk)))
        no = db.false()
        n = (re.sub(r"[',()/\]\[]", '', str(no)))
        await message.answer('В бота заходило:\n' + str(len_user) + ' ' + str(a) + '\nГолосование:\n' + '👍' + ' ' + b
                             + '\n👎' + ' ' + n)
    else:
        await message.answer('Нажмите на значок клавиатуры, чтобы отправить сообщение')


def do_work(count):
    if 1 < count % 10 < 5 and count // 10 != 1:
        a = "человека"
        return a
    else:
        a = "человек"
        return a


@aiocron.crontab('*/1 * * * *')
async def msg_two():
    try:
        for i in db.date_2():
            msg_2 = (re.sub(r"[',()]", '', str(i)))
            time.sleep(0.1)
            await bot.send_photo(msg_2, types.InputFile("image/1.png"))
    except ChatNotFound:
        pass

    try:
        for n in db.date_2_1():
            msg_2_1 = (re.sub(r"[',()]", '', str(n)))
            time.sleep(0.1)
            await bot.send_message(msg_2_1, 'Делюсь с тобой вступительным видео для курса'
                                            ' «Дыхание Жизни». Так Ты сможешь '
                                            'познакомиться со мной ближе.')
    except ChatNotFound:
        pass

    try:
        for g in db.date_3():
            msg_3 = (re.sub(r"[',()]", '', str(g)))
            time.sleep(0.1)
            await bot.send_video(msg_3, 'BAACAgIAAxkBAAMEYpOYb_lPeDMlKcTSDdrM0uZDZjgAAmEYAAJF_plIG0FxQsYKMkckBA',
                                 caption='Приветствую и желаю улыбки твоему сердцу и ясности твоему дыханию!')
            time.sleep(0.1)
            await bot.send_message(msg_3, ' Помоги мне узнать, понравилось ли тебе видео!', reply_markup=in_key)
    except ChatNotFound:
        pass

    try:
        for q in db.date_4():
            msg_4 = (re.sub(r"[',()]", '', str(q)))
            time.sleep(0.1)
            await bot.send_message(msg_4, 'Сердечный привет!')
    except ChatNotFound:
        pass

    try:
        for w in db.date_4_1():
            msg_4_1 = (re.sub(r"[',()]", '', str(w)))
            time.sleep(0.1)
            await bot.send_photo(msg_4_1, types.InputFile("image/4.png"),
                                 caption='Курс «Дыхание Жизни» я написала на Бали,'
                                         ' вдохновлённая идеей создать'
                                         ' универсальный инструмент для людей, '
                                         'познающих себя и желающих улучшить'
                                         ' качество своей жизни и здоровья.'
                                         ' И у меня получилось! 😉 Программа курса'
                                         ' рассчитана на семь дней регулярных'
                                         ' занятий. Практики записаны с учётом'
                                         ' быстрого темпа современной жизни и'
                                         ' поэтому занимают всего 20 минут перед'
                                         ' сном или после пробуждения. Всё, что'
                                         ' нужно, это наушники и горизонтальная '
                                         'поверхность. Минимум усилий и максимум'
                                         ' расслабления. Слушать и делать. Точно'
                                         ' легко. Думаю, что сейчас самое время '
                                         'начать. Желаю тебе кайфануть по полной!<a href="https://mahimalife.ru/"> Начнем?</a>',
                                 parse_mode=types.ParseMode.HTML)
    except ChatNotFound:
        pass

    try:
        for e in db.date_5():
            msg_5 = (re.sub(r"[',()]", '', str(e)))
            time.sleep(0.1)
            await bot.send_photo(msg_5, types.InputFile("image/5.png"), caption='Продолжу со своей историей 🙂')
    except ChatNotFound:
        pass

    try:
        for r in db.date_5_1():
            msg_5_1 = (re.sub(r"[',()]", '', str(r)))
            time.sleep(0.1)
            await bot.send_message(
                msg_5_1, 'Я вернулась в Москву специально, чтобы записать курс «Дыхание Жизни»' \
                         ' в профессиональной студии звукозаписи. В процессе я использовала' \
                         ' уникальные инструменты, камертон частоты ОМ, звуки чаши, метроном,' \
                         ' дыхание океана, моё дыхание для твоей поддержки в ведении, мой голос' \
                         ' и чарующий звук гитары для раскрытия твоего сердца. Семь треков, ' \
                         'расположенных в специальном порядке, позволяют практикующему перейти ' \
                         'на глубокие слои подсознания и трансформировать текущие задачи на тонком' \
                         ' энергетическом уровне. Действие этого инструмента для трансформации' \
                         ' вызывает у меня истинный восторг!!! Желаю тебе освоить курс и получить' \
                         ' все дары жизни.<a href="https://mahimalife.ru/"> Вперед!</a> ',
                parse_mode=types.ParseMode.HTML)
    except ChatNotFound:
        pass

    try:
        for y in db.date_6():
            msg_6 = (re.sub(r"[',()]", '', str(y)))
            time.sleep(0.1)
            await bot.send_photo(msg_6, types.InputFile("image/6.png"),
                                 caption='Приветствую всей собой! Представляешь, что можно дышать добротой? Попробуй! '
                                         'Сделай вдох, принимая доброту этого мира! Сделай выдох, пропуская сквозь себя'
                                         ' доброту мира! Наполненность и прилив сил обеспечены! А мой курс тебе поможет'
                                         ' закрепить доброту мира внутри и снаружи.'
                                         ' <a href="https://mahimalife.ru/"> Дыши!!!</a> '
                                 , parse_mode=types.ParseMode.HTML)
    except ChatNotFound:
        pass
    try:
        for h in db.date_7():
            msg_7 = (re.sub(r"[',()]", '', str(h)))
            time.sleep(0.1)
            await bot.send_photo(msg_7, types.InputFile("image/7.jpg"), caption='Привет 😊')
    except ChatNotFound:
        pass
    try:
        for o in db.date_7_2():
            msg_7_2 = (re.sub(r"[',()]", '', str(o)))
            time.sleep(0.1)
            await bot.send_message(
                msg_7_2, 'Когда мне плохо, я начинаю глубже дышать! Когда мне хорошо, я начинаю глубже дышать!!!'
                         ' Дыхание — главный инструмент, через который мы можем лучше познать жизнь и быстро и легко'
                         ' решить свои задачи '
                         'в жизни.<a href="https://mahimalife.ru/"> Дышим</a> вместе! ', parse_mode=types.ParseMode.HTML)
    except ChatNotFound:
        pass


@dp.message_handler(content_types='text', state=FSMail_user.sms)
async def msg(message: types.Message, state: FSMContext):
    global data
    async with state.proxy() as data:
        data['text'] = message.text
        await state.finish()
        await message.answer('Ваше сообщение: ' + data['text'] + '\nДля отправки сообщения нажми кнопку отправить!',
                             reply_markup=send_msg)


@dp.message_handler(content_types='text', state=FSMail_send_user.sms_user)
async def msg_end(message: types.Message, state: FSMContext):
    global data_1
    async with state.proxy() as data_1:
        data_1['text'] = message.text
        await state.finish()
        await message.answer('Ваше сообщение: ' + data_1['text'] + '\nДля отправки сообщения нажми кнопку отправить!',
                             reply_markup=send_ok)


@dp.callback_query_handler(text='yes')
async def yes(call: types.CallbackQuery):
    await call.bot.send_photo(call.from_user.id, types.InputFile("image/3.png"))
    await call.bot.delete_message(call.from_user.id, call.message.message_id)
    tru = db.true()[0]
    a = int((re.sub(r"[',()/\]\[]", '', str(tru))))
    a += 1
    db.true_up(str(a))


@dp.callback_query_handler(text='no')
async def no(call: types.CallbackQuery):
    await call.bot.send_photo(call.from_user.id, types.InputFile("image/3.png"))
    await call.bot.delete_message(call.from_user.id, call.message.message_id)
    tru = db.false()[0]
    a = int((re.sub(r"[',()/\]\[]", '', str(tru))))
    a += 1
    db.fals_up(str(a))


@dp.callback_query_handler(text='back')
async def back_menu(call: types.CallbackQuery):
    await call.message.answer('Вы вернулись в главное меню!',reply_markup=key)
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)


@dp.callback_query_handler(text='send')
async def send_menu(call: types.CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    db.add_message(call.from_user.id, data['text'])
    await bot.send_message('id админа', 'У вас новое сообщение!')
    await call.message.answer('Вы отправили сообщение, скоро мы Вам ответим', reply_markup=key)


@dp.callback_query_handler(text='mail_ok')
async def send_user(call: types.CallbackQuery):
    await call.message.answer('Напишите сообщения для ответа')
    await FSMail_send_user.sms_user.set()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)


@dp.callback_query_handler(text='mail_no')
async def send_user(call: types.CallbackQuery):
    await call.message.answer('Сообщение удалено')
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    db.del_sub(id_sub)


@dp.callback_query_handler(text='mail_ok_sub')
async def back_menu(call: types.CallbackQuery):
    await call.message.answer('Вы ответили пользователю ')
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await bot.send_message(id_sub, 'Ответ на ваше сообщение:\n' + data_1['text'])
    db.del_sub(id_sub)


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
