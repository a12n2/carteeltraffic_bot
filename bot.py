from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = "7854283477:AAFPqBOplPvUN8yaiWNOXYf6Gre6-hT4YuY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Добро пожаловать в команду по арбитражу трафика!
Ты только что сделал шаг в мир, где каждый клик — это возможность, а каждая связка — путь к прибыли.

🚀 Здесь ты получишь:
— Поддержку от команды 24/7
— Актуальные офферы и проверенные схемы
— Гайды, инсайды и рабочие стратегии
— И, конечно, атмосферу роста и движения к результату

⚡️ Готов вливаться в трафик и зарабатывать? Погнали!")
    
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
