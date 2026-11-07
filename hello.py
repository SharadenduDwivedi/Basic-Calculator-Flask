from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")

def home():
    return "Hello World"

@app.route("/<name>")

def greet(name):
    return f"Hello {name}, How are you doing?"

def read_numbers():
    a = request.args.get("a")
    b = request.args.get("b")
    if a is None or b is None:
        return None, None, "a or b is not a number"
    try:
        return float(a), float(b), None
    except:
        return None, None, "a and b must be numbers"

def respond(operation,a,b, result):
    # print(f"{operation}: {a} and {b} ----> {result}")
    return jsonify({"operation": operation,"operands": f"{a} and {b}","result": result})

@app.route("/add")

# def add(*numbers):
#     sum = 0
#     for i in numbers:
#         sum += i
#     return f"The total sum is sum"

# def add():
#     a = request.args.get("a")
#     b = request.args.get("b")
#     total = float(a) + float(b)
#     return f"{a} + {b} is {total}"

def add():
    a,b, error = read_numbers()
    if error:
        return jsonify({"error":error}), 400
    return respond("addiion",a,b,a+b)

@app.route("/subtract")

# def subtract():
#     a = request.args.get("a")
#     b = request.args.get("b")
#     total = float(a) - float(b)
#     return f"{a} - {b} is {total}"

def subtract():
    a,b, error = read_numbers()
    if error:
        return jsonify({"error":error})
    return respond("subtraction",a,b,a-b)

@app.route("/multiply")

def multiply():
    a,b, error = read_numbers()
    if error:
        return jsonify({"error": error})
    return respond("multiplication",a,b, a*b)

@app.route("/divide")

def divide():
    a,b, error = read_numbers()
    if error:
        return jsonify({"error": error})
    if b == 0:
        return jsonify({"error": "cannot divide by zero"}), 400
    return respond("division", a,b, a/b)

if __name__ == '__main__':
    app.run(debug=True)