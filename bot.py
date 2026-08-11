import logging
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, ContextTypes

TOKEN = "8932643761:AAH80RD5-i-P1sksa9t-3WS368fNUdeE0ZM"

logging.basicConfig(level=logging.INFO)

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data.startswith("accept_"):
        user = query.from_user
        user_name = f"@{user.username}" if user.username else user.first_name
        
        # Берем текущее время
        accept_time = datetime.now().strftime("%H:%M")
        original_text = query.message.text

        status_update = (
            f"✅ <b>ПРИНЯТ В РАБОТУ</b>\n"
            f"🕒 <b>Время:</b> {accept_time}\n"
            f"👤 <b>Принял:</b> {user_name}"
        )

        new_text = original_text.replace("⏳ Статус: В обработке...", status_update)

        updated_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🚗 В доставке", callback_data="delivering")]
        ])

        await query.edit_message_text(
            text=new_text, 
            parse_mode="HTML", 
            reply_markup=updated_keyboard
        )

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CallbackQueryHandler(handle_button))
    print("---------------------------------------")
    print("БОТ УСПЕШНО ЗАПУЩЕН И ЖДЕТ НАЖАТИЙ!")
    print("---------------------------------------")
    app.run_polling()