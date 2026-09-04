from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Routes for handling form submissions
@app.route('/add_income', methods=['POST'])
def add_income():
    source = request.form.get('source')
    amount = request.form.get('amount')
    # Process the income data here (e.g., store it in a database)
    print(f"Income added: Source - {source}, Amount - {amount}")
    return redirect(url_for('index'))

@app.route('/add_expense', methods=['POST'])
def add_expense():
    category = request.form.get('category')
    amount = request.form.get('amount')
    # Process the expense data here (e.g., store it in a database)
    print(f"Expense added: Category - {category}, Amount - {amount}")
    return redirect(url_for('index'))

@app.route('/set_goal', methods=['POST'])
def set_goal():
    goal_name = request.form.get('goal_name')
    target_amount = request.form.get('target_amount')
    # Process the goal data here (e.g., store it in a database)
    print(f"Goal set: Name - {goal_name}, Target Amount - {target_amount}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
