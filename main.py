from flask import Flask, render_template, request
import random
import re

app = Flask(__name__)

conversations = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "hi": ["Hi there!", "Hello!", "Hey"],
    "how are you": ["I'm good, thank you.", "Feeling great!", "I'm doing well."],
    "name": ["You can call me MathBot."],
    "what is maths": ["Mathematics, or math, is the study of numbers and "
             "how they are related to each other and to the real world."
             " Math is as important as language. In fact, "
             "people sometimes describe math as a kind of language."],
    "what is mathematics": ["Mathematics, or math, is the study of numbers and "
             "how they are related to each other and to the real world."
             " Math is as important as language. In fact, "
             "people sometimes describe math as a kind of language."],
    "joke": ["Why don't scientists trust atoms? Because they make up everything!",
             "Why did the math book look sad? Because it had too many problems.",
             "What did the triangle say to the circle? You're so pointless."],
    "what can you do": ["I can have conversations with you and provide math formulas. Just ask!",
                        "Make maths easier for you by giving you the formulas you need"],
    "father of maths ": ["Archimedes"],
    "math formula list": ["---MENU---<br> 1. Pythagoras Theorem<br>2. Perimeter of square<br>"
                          "3. Area of square<br>4. Perimeter of a rectangle<br>5. Area of a rectangle<br>"
                          "6. Perimeter of a circle<br>7. Circumference of circle<br>8. Area of a triangle<br>"
                          "9. Mean<br>10. Median<br>11. Mode<br>12. Linear Equation<br>13. Quadratic Equation<br>"
                          "14. Quadratic Formula<br>15. Volume of a sphere<br>16. Distance formula<br>"],
    "list of formulas": ["---MENU---<br> 1. Pythagoras Theorem<br>2. Perimeter of square<br>"
                          "3. Area of square<br>4. Perimeter of a rectangle<br>5. Area of a rectangle<br>"
                          "6. Perimeter of a circle<br>7. Circumference of circle<br>8. Area of a triangle<br>"
                          "9. Mean<br>10. Median<br>11. Mode<br>12. Linear Equation<br>13. Quadratic Equation<br>"
                          "14. Quadratic Formula<br>15. Volume of a sphere<br>16. Distance formula<br>"],
    "math formula": ["Sure! What formula do you need?"],
    "thank you": ["Glad i could help", "No problem", "Your Welcome"]
}

math_formulas = {
    "pythagoras theorem": "Pythagoras theorem: a^2 + b^2 = c^2",
    "quadratic formula": "Quadratic formula: (-b ± √(b^2 - 4ac)) / (2a)",
    "area of triangle": "Area of a triangle: 1/2 * base * height",
    "volume of sphere": "Volume of a sphere: (4/3) * π * r^3",
    "distance formula": "Distance formula: √((x2 - x1)^2 + (y2 - y1)^2)",
    "perimeter of a circle": "Perimeter of a circle = πr^2 ",
    "circumference of circle": "Circumference of circle: 2πr ",
    "mean": "Mean = sum of observations/number of observations ",
    "median": "Median = the mid value",
    "mode": "Mode = recurring number",
    "perimeter of a square": "Perimeter of a square = 4a",
    "area of square": "Area of a square = a^2",
    "perimeter of a rectangle": "Perimeter of a rectangle = 2*(length * breadth)",
    "area of a rectangle": "Area of a rectangle = length * breadth",
    "linear equation": "Linear equation = ax + b = c",
    "quadratic equation": "Quadratic equation = ax^2 + bx + c = 0",
}


def respond_to_conversation(message):
    for pattern, responses in conversations.items():
        if re.search(pattern, message, re.IGNORECASE):
            return random.choice(responses)

    return None


def get_math_formula(message):
    for pattern, formula in math_formulas.items():
        if re.search(pattern, message, re.IGNORECASE):
            return formula
        else:
            print("I'm sorry! I do not have that formula.")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']
    response = respond_to_conversation(user_message)
    if response:
        return response
    else:
        math_formula = get_math_formula(user_message)
        if math_formula:
            return math_formula
        else:
            return "I'm sorry, I don't understand that."


if __name__ == '__main__':
    app.run(debug=True)
