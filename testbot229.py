#TELEGRAM_TOKEN = "6497931798:AAGuwE4WJ26yrPy5uwSh5E_4NWPl_LTodZ8"

from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, keyboardbutton
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters
from pdfminer.high_level import extract_text
from difflib import SequenceMatcher

TELEGRAM_TOKEN = "6497931798:AAGuwE4WJ26yrPy5uwSh5E_4NWPl_LTodZ8"

RESPONSES_FILE = "responses.txt"

WELCOME_MESSAGE = "Привіт!\nЯ бот, який спілкується в стилі Івана Франка\nЯ все ще в розробці, тому можу відповідати не так як задумано"

# Загрузка ответов из файла
def load_responses(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    responses = {}
    for line in lines:
        line = line.replace("/", "\n")
        parts = line.strip().split("|")
        if len(parts) == 2:
            responses[parts[0].lower()] = parts[1]
    return responses

# Функция для определения сходства строк
def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Функция для поиска наилучшего соответствия запросу в словаре ответов
def find_best_match(query, response_dict, threshold=0.8):
    best_match = max(response_dict.keys(), key=lambda x: similarity(query.lower(), x.lower()))
    if similarity(query.lower(), best_match.lower()) > threshold:
        return response_dict[best_match]
    else:
        return None

responses_dict = load_responses(RESPONSES_FILE)

# Функция для обработки команды /start
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        ["Привіт", "Як життя?", "Яким було твоє основне заняття?"],
        ["Ким були твої батьки?", "Коли і де ти народився"],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard)
    update.message.reply_text(WELCOME_MESSAGE, reply_markup=reply_markup)

# Функция для обработки текстовых сообщений
def handle_messages(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text.lower()

    # Ищем наилучший вариант в словаре
    best_match_response = find_best_match(user_input, responses_dict)

    # Если нашли подходящий ответ, отправляем его
    if best_match_response:
        update.message.reply_text(best_match_response)
    else:
        update.message.reply_text("Вибачте, я поки не можу обробити цей запит")

def main() -> None:
    updater = Updater(token=TELEGRAM_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_messages))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
