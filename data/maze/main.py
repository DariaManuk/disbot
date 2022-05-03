from telegram import ReplyKeyboardMarkup

from map_game import change_level
from level_maps import level_num
from player_move import *
from ray_casting import ray_casting

# TOKEN = '5116714628:AAEoIs6Lfm6MwqxSNdB4usb6fMYL_GcOYAQ'
reply_keyboard_walking = [['w'],
                          ['a', 's', 'd'],
                          ['l', 'r'],
                          ['change_level']]
reply_keyboard_level = [[str(i) for i in range(1, level_num + 1)]]
# print(reply_keyboard_level)
markup_walking = ReplyKeyboardMarkup(reply_keyboard_walking, one_time_keyboard=False)
markup_level = ReplyKeyboardMarkup(reply_keyboard_level, one_time_keyboard=True)

maze_mode = "not_active"


def maze_start(update, context):
    global maze_mode
    maze_mode = "changing_level"
    new_level(update, context)


def new_level(update, context):
    global maze_mode
    maze_mode = "changing_level"
    update.message.reply_text(
        f'выбери уровень с 1 по {level_num}.\n для смена уровня просто пиши цифру.')


def echo(update, context):
    global maze_mode
    if maze_mode == "changing_level":
        if update.message.text.isdigit():
            number_level = int(update.message.text)
            if number_level > level_num:
                update.message.reply_text('Собака пиши команды')
            else:
                change_level(number_level)
                update.message.reply_text('уровень изменён')
                maze_mode = "active"
                ray_casting(player_pos, ANGELES[player_angle])
                update.message.reply_text(f"pos:{str(player_pos)} angle:{player_angle * 90}")
                context.bot.send_photo(update.message.chat_id, photo=open('6.png', 'rb'),
                                       reply_markup=markup_walking)
    else:
        update.message.reply_text('Собака пиши команды')


def forward(update, context):
    if maze_mode == "active":
        move_forward(player_pos, player_angle)
        # print(player_pos, ANGELES[player_angle])
        win_bool = ray_casting(player_pos, ANGELES[player_angle])
        update.message.reply_text(f"pos:{str(player_pos)} angle:{player_angle * 90}")
        context.bot.send_photo(update.message.chat_id, photo=open('6.png', 'rb'),
                               reply_markup=markup_walking)
        if win_bool:
            update.message.reply_text(
                f'красава')
            new_level(update, context)


def back(update, context):
    if maze_mode == "active":
        move_back(player_pos, player_angle)
        # print(player_pos, ANGELES[player_angle])
        win_bool = ray_casting(player_pos, ANGELES[player_angle])
        update.message.reply_text(f"pos:{str(player_pos)} angle:{player_angle * 90}")
        context.bot.send_photo(update.message.chat_id, photo=open('6.png', 'rb'),
                               reply_markup=markup_walking)
        if win_bool:
            update.message.reply_text(f'красава')
            new_level(update, context)


def right(update, context):
    if maze_mode == "active":
        move_right(player_pos, player_angle)
        # print(player_pos, ANGELES[player_angle])
        win_bool = ray_casting(player_pos, ANGELES[player_angle])
        update.message.reply_text(f"pos:{str(player_pos)} angle:{player_angle * 90}")
        context.bot.send_photo(update.message.chat_id, photo=open('6.png', 'rb'),
                               reply_markup=markup_walking)
        if win_bool:
            update.message.reply_text('красава')
            new_level(update, context)


def left(update, context):
    if maze_mode == "active":
        move_left(player_pos, player_angle)
        # print(player_pos, ANGELES[player_angle])
        win_bool = ray_casting(player_pos, ANGELES[player_angle])
        update.message.reply_text(f"pos:{str(player_pos)} angle:{player_angle * 90}")
        context.bot.send_photo(update.message.chat_id, photo=open('6.png', 'rb'),
                               reply_markup=markup_walking)
        if win_bool:
            update.message.reply_text(
                f'красава')
            new_level(update, context)


def angle_right(update, context):
    if maze_mode == "active":
        global player_angle
        player_angle += 1
        player_angle %= 4
        # print(player_pos, ANGELES[player_angle])
        win_bool = ray_casting(player_pos, ANGELES[player_angle])
        update.message.reply_text(f"pos:{str(player_pos)} angle:{player_angle * 90}")
        context.bot.send_photo(update.message.chat_id, photo=open('6.png', 'rb'),
                               reply_markup=markup_walking)
        if win_bool:
            update.message.reply_text(
                f'красава')
            new_level(update, context)


def angle_left(update, context):
    if maze_mode == "active":
        global player_angle
        player_angle -= 1
        player_angle %= 4
        # print(player_pos, ANGELES[player_angle])
        win_bool = ray_casting(player_pos, ANGELES[player_angle])
        update.message.reply_text(f"pos:{str(player_pos)} angle:{player_angle * 90}")
        context.bot.send_photo(update.message.chat_id, photo=open('6.png', 'rb'),
                               reply_markup=markup_walking)
        if win_bool:
            update.message.reply_text(
                f'красава')
            new_level(update, context)


def text_to_command_maze(text, player_pos, player_angle, map):
    if text == "w":
        return move_forward(player_pos, player_angle, map)
    elif text == "s":
        return move_back(player_pos, player_angle, map)
    elif text == "d":
        return move_right(player_pos, player_angle, map)
    elif text == "a":
        return move_left(player_pos, player_angle, map)
    elif text == "l":
        player_angle -= 1
        player_angle %= 4
        return player_pos, player_angle
    elif text == "r":
        player_angle += 1
        player_angle %= 4
        return player_pos, player_angle
    else:
        return None, None

# def main():
#     # Создаём объект updater.
#     # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
#     updater = Updater(TOKEN, use_context=True)
#
#     # Получаем из него диспетчер сообщений.
#     dp = updater.dispatcher
#
#     # Создаём обработчик сообщений типа Filters.text
#     # из описанной выше функции echo()
#     # После регистрации обработчика в диспетчере
#     # эта функция будет вызываться при получении сообщения
#     # с типом "текст", т. е. текстовых сообщений.
#     text_handler = MessageHandler(Filters.text, echo)
#     dp.add_handler(CommandHandler("w", forward))
#     dp.add_handler(CommandHandler("s", back))
#     dp.add_handler(CommandHandler("d", right))
#     dp.add_handler(CommandHandler("a", left))
#     dp.add_handler(CommandHandler("r", angle_right))
#     dp.add_handler(CommandHandler("l", angle_left))
#     dp.add_handler(CommandHandler("change_level", new_level))
#     dp.add_handler(text_handler)
#     updater.start_polling()
#     updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
# if __name__ == '__main__':
#     main()
