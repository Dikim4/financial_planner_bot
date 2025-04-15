import logging
import json
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, ConversationHandler

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants for conversation states
CONFIG_CATEGORY, CONFIG_AMOUNT, LOG_TYPE, LOG_CATEGORY, LOG_AMOUNT = range(5)

# Directory for storing user data
DATA_DIR = 'user_data'
os.makedirs(DATA_DIR, exist_ok=True)

# Helper functions for file management
def get_user_file(user_id):
    return os.path.join(DATA_DIR, f'{user_id}.json')

def load_user_data(user_id):
    filepath = get_user_file(user_id)
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    else:
        return {'income': 0, 'budgets': {}, 'logs': [], 'notifications': True}

def save_user_data(user_id, data):
    with open(get_user_file(user_id), 'w') as f:
        json.dump(data, f, indent=2)

# Command Handlers
async def start(update: Update, context: CallbackContext):
    user = update.effective_user
    await update.message.reply_text(f"Hello {user.first_name}! I'm your Financial Planner Bot. Use /help to see commands.")

async def help_command(update: Update, context: CallbackContext):
    help_text = (
        "/start - Welcome message\n"
        "/help - Show this help\n"
        "/config - Configure income/budgets\n"
        "/log - Log income/expense\n"
        "/summary - View summary\n"
        "/notifyon - Enable notifications\n"
        "/notifyoff - Disable notifications"
    )
    await update.message.reply_text(help_text)

async def summary(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    data = load_user_data(user_id)
    income = data['income']
    total_expenses = sum(l['amount'] for l in data['logs'] if l['type'] == 'expense')
    balance = income - total_expenses
    
    response = f"Income: {income}\nTotal Expenses: {total_expenses}\nBalance: {balance}\n\nBudgets:\n"
    
    for cat, amt in data['budgets'].items():
        spent = sum(l['amount'] for l in data['logs'] if l['type'] == 'expense' and l['category'] == cat)
        response += f"{cat}: {spent}/{amt}\n"

    await update.message.reply_text(response)

# Conversation Handlers
async def config_start(update: Update, context: CallbackContext):
    await update.message.reply_text("Enter the category you want to set a budget for (or type 'income' to set monthly income):")
    return CONFIG_CATEGORY

async def config_category(update: Update, context: CallbackContext):
    context.user_data['config_category'] = update.message.text.strip().lower()
    await update.message.reply_text(f"Enter the amount for {context.user_data['config_category']}:")
    return CONFIG_AMOUNT

async def config_amount(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    amount = float(update.message.text.strip())
    category = context.user_data['config_category']
    data = load_user_data(user_id)
    if category == 'income':
        data['income'] = amount
    else:
        data['budgets'][category] = amount
    save_user_data(user_id, data)
    await update.message.reply_text(f"Set {category} to {amount} successfully.")
    return ConversationHandler.END

# Logging Handlers
async def log_start(update: Update, context: CallbackContext):
    await update.message.reply_text("Log type? (income/expense):")
    return LOG_TYPE

async def log_type(update: Update, context: CallbackContext):
    context.user_data['log_type'] = update.message.text.strip().lower()
    await update.message.reply_text("Enter category:")
    return LOG_CATEGORY

async def log_category(update: Update, context: CallbackContext):
    context.user_data['log_category'] = update.message.text.strip().lower()
    await update.message.reply_text("Enter amount:")
    return LOG_AMOUNT

async def log_amount(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    amount = float(update.message.text.strip())
    log_entry = {
        'type': context.user_data['log_type'],
        'category': context.user_data['log_category'],
        'amount': amount
    }
    data = load_user_data(user_id)
    data['logs'].append(log_entry)
    save_user_data(user_id, data)
    await update.message.reply_text("Entry logged successfully.")
    return ConversationHandler.END

# Notifications Handlers
async def notify_on(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    data = load_user_data(user_id)
    data['notifications'] = True
    save_user_data(user_id, data)
    await update.message.reply_text("Notifications enabled.")

async def notify_off(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    data = load_user_data(user_id)
    data['notifications'] = False
    save_user_data(user_id, data)
    await update.message.reply_text("Notifications disabled.")

# Main function to start the bot
def main():
    TOKEN = "8137061709:AAG3QiPIKT86kLNVJmgk4Pu5Z3OoCEvJMrg"
    app = Application.builder().token(TOKEN).build()

    # Register command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("summary", summary))
    app.add_handler(CommandHandler("notifyon", notify_on))
    app.add_handler(CommandHandler("notifyoff", notify_off))

    # Config conversation
    config_conv = ConversationHandler(
        entry_points=[CommandHandler("config", config_start)],
        states={
            CONFIG_CATEGORY: [MessageHandler(filters.TEXT & ~filters.COMMAND, config_category)],
            CONFIG_AMOUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, config_amount)],
        },
        fallbacks=[],
    )
    app.add_handler(config_conv)

    # Log conversation
    log_conv = ConversationHandler(
        entry_points=[CommandHandler("log", log_start)],
        states={
            LOG_TYPE: [MessageHandler(filters.TEXT & ~filters.COMMAND, log_type)],
            LOG_CATEGORY: [MessageHandler(filters.TEXT & ~filters.COMMAND, log_category)],
            LOG_AMOUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, log_amount)],
        },
        fallbacks=[],
    )
    app.add_handler(log_conv)

    # Run the bot
    app.run_polling()

if __name__ == "__main__":
    main()

