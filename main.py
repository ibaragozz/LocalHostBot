import telebot

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота, который вы получили от BotFather
TOKEN = '7469710583:AAE5j_bKHvtIY6xJXfjvwN7i73N3X1VM4vw'
bot = telebot.TeleBot(TOKEN)


# Обработчик сообщений, который реагирует на все текстовые сообщения
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "этот бот лежит на локальном сервере с автозапуском")


# Запуск бота
if __name__ == '__main__':
    print("Бот запущен и ждет сообщений...")
    bot.infinity_polling()