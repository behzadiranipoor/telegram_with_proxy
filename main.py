
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# تنظیم پروکسی برای کل سیستم
import os
os.environ['HTTP_PROXY'] = 'socks5://127.0.0.1:12334'
os.environ['HTTPS_PROXY'] = 'socks5://127.0.0.1:12334'

TOKEN = "8314129452:AAEBpb3G0dJIuRGDuSQCixzD88ULeEuZYB0"

app = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.message.from_user.first_name
    await update.message.reply_text(f"slam {name}")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    await update.message.reply_text(f"you said {user_text}")

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("robot is running with proxy...")
app.run_polling()


