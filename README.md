# 💸 Telegram Financial Planner Bot

A personal finance planner Telegram bot built with Python & Telegram Bot API.

## 🚀 Features

- Set income and budgets per category
- Log income & expenses with category
- View balance, budget usage, and remaining funds
- Notifications for summaries and budget alerts
- Basic commands:
  - `/start` – Greet the user
  - `/help` – List all commands
  - `/config` – Configure income/budget
  - `/log` – Log income or expense
  - `/summary` – View financial summary
  - `/notifyon` – Enable notifications
  - `/notifyoff` – Disable notifications

## 🧑‍💻 Tech Stack

- Python 3
- python-telegram-bot library

## 📷 Screenshots

_(Добавь свои скриншоты сюда после тестов!)_

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/financial_planner_bot.git
cd financial_planner_bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Insert your Bot Token

Replace the value of `TOKEN` in `bot.py` with your actual bot token from [@BotFather](https://t.me/BotFather).

### 4. Run the bot

```bash
mkdir user_data
python bot.py
```

## 📂 File Structure

- `bot.py` – Main bot logic
- `user_data/` – Stores user data in JSON format
- `requirements.txt` – Python dependencies
- `README.md` – Setup instructions
- `.gitignore` – Prevents uploading user data & cache

## 👥 Authors

Group of 2 students – _Add your names here!_

## 📦 How to Submit

1. Push to GitHub/GitLab
2. Include:
   - ✅ Clean and commented code
   - ✅ README with setup and features
   - ✅ Screenshots of the bot in use
