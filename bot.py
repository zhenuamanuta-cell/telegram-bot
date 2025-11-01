from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 🔑 Твій токен
TOKEN = "8507837875:AAF4Fw-F6VFHGVc-uCRDiRdJIecsez9zsic"

# 🔗 Посилання на канал
CHANNEL_LINK = "https://t.me/+2GqP5vz-m4M1Y2Ji"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Сюда👇\n{CHANNEL_LINK}"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("✅ Бот запущено...")
app.run_polling()


