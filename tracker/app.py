from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

# In-memory data storage
expenses = []
goals = []
subscriptions = []
categories = ['Food', 'Transport', 'Entertainment']
currency_conversion = {'USD': 1, 'EUR': 0.85, 'INR': 74.57}

# AI-based insights
def ai_insights():
    total_spent = sum(exp['amount'] for exp in expenses)
    if total_spent > 500:
        return "Warning: You have spent more than $500 this month!"
    return "Your spending is under control."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_expense', methods=['POST'])
def add_expense():
    category = request.form['category']
    amount = float(request.form['amount'])
    currency = request.form['currency']
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    amount_in_usd = amount * currency_conversion[currency]
    expenses.append({'category': category, 'amount': amount_in_usd, 'currency': currency, 'date': date})
    return 'Expense added!'

@app.route('/summary')
def summary():
    total_expenses = sum(exp['amount'] for exp in expenses)
    insights = ai_insights()
    return jsonify({'total_expenses': total_expenses, 'insights': insights})

@app.route('/set_goal', methods=['POST'])
def set_goal():
    goal = request.form['goal']
    goals.append(goal)
    return 'Goal added!'

@app.route('/add_subscription', methods=['POST'])
def add_subscription():
    subscription = request.form['subscription']
    subscriptions.append(subscription)
    return 'Subscription added!'

if __name__ == '__main__':
    app.run(debug=True)
