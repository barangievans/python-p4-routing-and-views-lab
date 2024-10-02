from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>', 200

@app.route('/print/<parameter>')
def print_parameter(parameter):
    print(parameter)  # Print to console
    return parameter, 200

@app.route('/count/<int:parameter>')
def count(parameter):
    count_output = '\n'.join(str(i) for i in range(parameter)) + '\n'
    return count_output, 200

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math_operation(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return Response("Cannot divide by zero", status=400)
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return Response("Unsupported operation", status=400)

    return str(result), 200

if __name__ == '__main__':
    app.run(debug=True)
