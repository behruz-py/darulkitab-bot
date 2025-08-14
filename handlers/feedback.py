from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler
from storage import add_feedback

ASK_FEEDBACK = 1


# 💬 Fikr olishni boshlash
async def ask_feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [[
        InlineKeyboardButton("❌ Bekor qilish", callback_data="cancel_feedback"),
        InlineKeyboardButton("🏠 Asosiy menyu", callback_data="home"),
    ]]

    await query.edit_message_text(
        text=(
            "💬 Fikringizni yozib yuboring. Taklif, tanqid yoki minnatdorchilik bo‘lishi mumkin.\n\n"
            "✍️ Yozib bo‘lgach, yuboring.\n\n"
            "👇 Pastdagi tugmalar orqali bekor qilishingiz yoki menyuga qaytishingiz mumkin."
        ),
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    return ASK_FEEDBACK


# ✅ Fikrni saqlash (DB)
async def save_feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = (update.message.text or "").strip()

    add_feedback(
        user_id=user.id,
        name=f"{user.first_name or ''} {user.last_name or ''}".strip(),
        username=user.username or "",
        text=text
    )

    await update.message.reply_text("✅ Fikringiz uchun rahmat!")

    keyboard = [[InlineKeyboardButton("🏠 Asosiy menyu", callback_data="home")]]
    await update.message.reply_text(
        "Yana nimadir qilishni istaysizmi?",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    return ConversationHandler.END


# 🚫 Bekor qilish
async def cancel_feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [[InlineKeyboardButton("🏠 Asosiy menyu", callback_data="home")]]
    await query.edit_message_text(
        "❌ Fikr bildirish bekor qilindi.\n\nQuyidagi tugma orqali asosiy menyuga qaytishingiz mumkin:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    return ConversationHandler.END
