
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

OPERATIONS = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b,
}

SYMBOLS = {
    "add": "+",
    "subtract": "-",
    "multiply": "*",
    "divide": "/",
}

def calculate(operation, a_text, b_text):
    if operation not in OPERATIONS:
        return None, "Unknown Operation"

    try:
        a, b = float(a_text), float(b_text)
    except (TypeError, ValueError):
        return None, "Please enter valid numbers"

    if operation == "divide" and b == 0:
        return None, "Cannot divide by zero"

    return OPERATIONS[operation](a, b), None


@app.route("/api/<operation>")
def api(operation):
    result, error = calculate(
        operation,
        request.args.get("a"),
        request.args.get("b")
    )

    if error:
        return jsonify({"error": error}), 400

    return jsonify({"operation": operation, "result": result})


# Store calculation history
equations = []

@app.route("/", methods=["GET", "POST"])
def home():
    result = error = None

    if request.method == "POST":
        operation = request.form["operation"]
        a = request.form["a"]
        b = request.form["b"]

        result, error = calculate(operation, a, b)

        if error is None:
            equation = f"{a} {SYMBOLS[operation]} {b} = {result}"
            equations.append(equation)

    return render_template(
        "index.html",
        result=result,
        error=error,
        equations=equations
    )


if __name__ == "__main__":
    app.run(debug=True)
