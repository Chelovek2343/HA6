from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

# === НАСТРОЙКИ ===
TOKEN = "ТВОЙ_ТОКЕН_БОТА"
AUTHORIZED_USER_ID = 123456789  # Замени на свой Telegram ID

# === КНОПКИ ===
keyboard = ReplyKeyboardMarkup(
    [["/shutdown"]],
    resize_keyboard=True,
    one_time_keyboard=False
)

# === ПРИВЕТСТВИЕ ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != AUTHORIZED_USER_ID:
        await update.message.reply_text("Нет доступа.")
        return
    await update.message.reply_text(
        "Привет! Нажми кнопку ниже, чтобы выключить компьютер:",
        reply_markup=keyboard
    )

# === ВЫКЛЮЧЕНИЕ ===
async def shutdown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != AUTHORIZED_USER_ID:
        await update.message.reply_text("Нет доступа.")
        return
    await update.message.reply_text("Компьютер выключается...")
    os.system("shutdown /s /t 0")

# === ЗАПУСК БОТА ===
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("shutdown", shutdown_command))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^/shutdown$"), shutdown_command))

print("Бот запущен.")
app.run_polling()
