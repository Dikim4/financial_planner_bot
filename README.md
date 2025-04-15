# 💸 Telegram Financial Planner Bot

This is a Telegram bot built in Python that helps users manage their finances by tracking income, expenses, and budgets. The bot allows users to configure their income, set budgets for different categories, log transactions, and view their financial summary. Additionally, it supports notifications for budget alerts and daily/weekly summaries.


## 🚀 Features

-Configure Income & Budgets: Users can set their monthly income and configure budgets for different expense categories.
-Log Expenses & Income: Log transactions as either income or expenses, with the ability to categorize them.
-View Balance & Budget Summaries: Get an overview of your total income, expenses, and remaining balance. Check your progress with category-specific budgets.
-Push Notifications: Enable or disable notifications for daily/weekly summaries and budget alerts to stay on top of your finances.
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

### 1. Start and help
![StartHelp](screenshots/starthelp.jpg)

### 2. Configuring Income
![Income](screenshots/config.jpg)

### 3. Logging and Summary
![Logsum](screenshots/logsum.jpg)

### 4. Notifications off/on
![Nitif](screenshots/notif.jpg)


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

## 👥 Author
Kim Diana 

