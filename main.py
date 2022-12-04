# Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения
# и PIP Прикрутить бота к задачам с предыдущего семинара: Создать калькулятор для работы
# с рациональными и комплексными числами, организовать меню, добавив в него систему
# логирования


from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token(token_telegram).build()

app.add_handler(CommandHandler("div", div_command))
app.add_handler(CommandHandler('diff', diff_command))
app.add_handler(CommandHandler('sum', sum_command))
app.add_handler(CommandHandler('help', help_command))
app.add_handler(CommandHandler('mul',mul_command))


print('server start')
app.run_polling()
