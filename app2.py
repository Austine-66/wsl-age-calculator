import datetime
from flask import Flask, request, render_template_string
from dateutil.relativedelta import relativedelta  # Makes exact age math incredibly easy

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Age Calculator</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f9; text-align: center; }
        .container { background: white; padding: 30px; border-radius: 10px; display: inline-block; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); }
        input { padding: 10px; margin: 10px; width: 200px; border: 1px solid #ccc; border-radius: 5px; }
        button { padding: 10px 20px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer; }
        button:hover { background-color: #0056b3; }
        .result { margin-top: 20px; font-weight: bold; color: #28a745; font-size: 1.2em; }
    </style>
</head>
<body>
    <div class="container">
        <h2>--- Welcome to your WSL Python Web App ---</h2>
        <form method="POST">
            <input type="text" name="name" placeholder="What is your name?" required><br>
            <input type="date" name="birth_date" required><br>
            <button type="submit">Calculate Age</button>
        </form>

        {% if result1 %}
            <div class="result">
                <p>{{ result1 }}</p>
                <p>{{ result2 }}</p>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result1 = None
    result2 = None
    
    if request.method == "POST":
        name = request.form.get("name")
        birth_date_str = request.form.get("birth_date")
        
        birth_date = datetime.datetime.strptime(birth_date_str, "%Y-%m-%d").date()
        today = datetime.date.today()
        
        diff = relativedelta(today, birth_date)
        
        turning_age = today.year - birth_date.year
        
        result1 = f"Hello {name}! You are turning {turning_age} years old this calendar year."
        
        result2 = f"The current year is {today.year} and you were born in {birth_date.year}. This makes you exactly {diff.years} years, {diff.months} months, and {diff.days} days old today."

    return render_template_string(HTML_TEMPLATE, result1=result1, result2=result2)

if __name__ == "__main__":
    app.run(debug=True)
