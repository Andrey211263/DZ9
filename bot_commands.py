from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from spy import *


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/все вводим через пробел\n/diff\n/div\n/sum\n/mul\n')

# разность
async def diff_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    item = msg.split()
    x = float(item[1])
    y = float(item[2])
    await update.message.reply_text(f'{x} - {y} = {x-y}')

# сумма
async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    print(msg)
    item = msg.split()
    x = float(item[1])
    y = float(item[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')

# умножение
async def mul_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    item = msg.split()
    x = float(item[1])
    y = float(item[2])
    await update.message.reply_text(f'{x} + {y} = {x*y}')

# деление
async def div_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    item = msg.split()
    x = float(item[1])
    y = float(item[2])
    await update.message.reply_text(f'{x} / {y} = {x/y}')

    await update.message.reply_text(f'{x} + {y} = {x+y}')
