from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/home')
def welcome():
    return "welcome to flask"

@app.route('/cal', methods=["GET"])
def math_operator():
    operation=request.json["operation"]
    num1=request.json["number1"]
    num2=request.json["number2"]

    if operation == "add":
        result=num1+num2
    elif operation == "multiply":
        result=num1*num2
    elif operation == "divide":
        result=num1/num2
    else:
        result=num1-num2
    return result





print (__name__)

if __name__ == '__main__':
    app.run(debug=True)