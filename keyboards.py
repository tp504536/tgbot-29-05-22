from aiogram import types


key = types.ReplyKeyboardMarkup(resize_keyboard=True)
msg = types.KeyboardButton(text='Задать вопрос')
key.add(msg)

in_key =types.InlineKeyboardMarkup(row_width=1)
in_msg_1 = types.InlineKeyboardButton(text='Да, очень 😍',callback_data='yes')
in_msg_2 = types.InlineKeyboardButton(text='Чего-то не хватает 😕', callback_data='no')
in_key.add(in_msg_1).add(in_msg_2)


admin_key = types.ReplyKeyboardMarkup(resize_keyboard=True)
msg_admin = types.KeyboardButton(text='Входящие сообщения')
msg_static = types.KeyboardButton(text='Статистика')
admin_key.add(msg_admin).add(msg_static)


send_msg = types.InlineKeyboardMarkup(row_width=1)
all_msg = types.InlineKeyboardButton(text='Отправить', callback_data='send')
back = types.InlineKeyboardButton(text='Отмена', callback_data='back')
send_msg.add(all_msg).add(back)


ok = types.InlineKeyboardMarkup(row_width=1)
mail_ok = types.InlineKeyboardButton(text='Ответить', callback_data='mail_ok')
mail_no = types.InlineKeyboardButton(text='Не отвчеавть', callback_data='mail_no')
ok.add(mail_ok).add(mail_no)


send_ok = types.InlineKeyboardMarkup(row_width=1)
mai_sub_ok = types.InlineKeyboardButton(text='Отправить', callback_data='mail_ok_sub')
send_ok.add(mai_sub_ok).add(back)