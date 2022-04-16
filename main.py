from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup
from data import db_session
from data.users import User
from data.results import Results

b_start, b_menu, b_end_play, b_stop = 't', 'f', 'f', 'f'
db_session.global_init("db/bot.db")


def start(update, context):
    global b_start, b_menu, b_stop, b_end_play
    db_sess = db_session.create_session()
    a = [i.id_tg for i in db_sess.query(User).all()]
    if update.message.from_user.id not in a:
        user = User()
        user.id_tg = update.message.from_user.id
        user.username = update.message.from_user.username
        db_sess.add(user)
        db_sess.commit()
        result = Results(user=user)
        db_sess.add(result)
        db_sess.commit()
    if b_start == 't':
        reply_keyboard = [['/menu'], ['/stop']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
        update.message.reply_text(f'''Я бот с играми.\n
        Если хотите посмотреть меню нажмите - /menu .\n
        Если хотите остановить бота нажмите - /stop .''',
                                  reply_markup=markup)
        b_start = '0'
        b_menu, b_stop, b_end_play = 't', 't', 'f'
    elif b_start == '0':
        reply_keyboard = [['/menu'], ['/stop']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
        update.message.reply_text(f'''Бот уже активирован\n
                Если хотите посмотреть меню нажмите - /menu .\n
                Если хотите остановить бота нажмите - /stop .''',
                                  reply_markup=markup)
        b_start = '0'
        b_menu, b_stop, b_end_play = 't', 't', 'f'
    else:
        update.message.reply_text(f'''Бот уже активирован''')
        echo(update, context)


def echo(update, context):
    update.message.reply_text(f'Ответьте пожалуйста на сообщение.')
    if b_start == '0':
        return start(update, context)
    elif b_end_play == '0':
        return end_play(update, context)
    elif b_stop == 'f':
        return stop(update, context)


def stop(update, context):
    global b_start, b_menu, b_stop, b_end_play
    if b_stop == 't':
        reply_keyboard = [['/start']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
        update.message.reply_text(
            f'''Бот выключен. Спасибо за игру.\n
            Чтобы заново активировать бота нажмите - /start .''',
            reply_markup=markup)
        b_start, b_menu, b_end_play, b_stop = 't', 'f', 'f', 'f'
    else:
        reply_keyboard = [['/start']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
        update.message.reply_text(
            f'''Бот уже выключен.\n
            Чтобы заново активировать бота нажмите - /start .''',
            reply_markup=markup)


def end_play(update, context):
    global b_menu, b_stop, b_end_play, b_start
    if b_end_play == 't':
        reply_keyboard = [['/menu'], ['/stop']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
        update.message.reply_text(f'''Игра досрочно завершена. Результаты не занесены в рейтинг.\n
        Если хотите посмотреть меню нажмите - /menu .\n
        Если хотите остановить бота нажмите - /stop .''',
                                  reply_markup=markup)
        b_menu, b_end_play, b_stop, b_start = 't', '0', 't', 'f'
    elif b_end_play == '0':
        reply_keyboard = [['/menu'], ['/stop']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
        update.message.reply_text(f'''Игра уже завершена.\n
                Если хотите посмотреть меню нажмите - /menu .\n
                Если хотите остановить бота нажмите - /stop .''',
                                  reply_markup=markup)
        b_menu, b_end_play, b_stop, b_start = 't', '0', 't', 'f'
    else:
        update.message.reply_text(f'''Вы ещё не начали играть.''')
        echo(update, context)


def menu(update, context):
    global b_menu, b_stop, b_end_play, b_start
    if b_menu in ['t', '0']:
        reply_keyboard = [['/cities', '/maze', '/xo'], ['/stop']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
        update.message.reply_text(f'''Выберите игру:\n
        города - /cities\n
        крестики-нолики - /xo\n
        лабиринт - /maze\n
        Выключить бота - /stop\n''',
                                  reply_markup=markup)
        b_menu, b_end_play, b_stop, b_start = '0', 'f', 't', 'f'
    else:
        update.message.reply_text(f'''В данный момент нельзя открыть меню.''')
        echo(update, context)


def main():
    updater = Updater('5104954005:AAFW-n0oIGM7ZqHprL8B-O4szvpjMVhx6yo', use_context=True)
    dp = updater.dispatcher
    text_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("stop", stop))
    dp.add_handler(CommandHandler("end_play", end_play))
    dp.add_handler(CommandHandler("menu", menu))
    dp.add_handler(text_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
