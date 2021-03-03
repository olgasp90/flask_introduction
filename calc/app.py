# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/add')
def add_nums():
    """return the sum of a and b parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)


@app.route('/sub')
def sub_nums():
    """return the difference of a and b parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)

    return str(result)

@app.route('/mult')
def mult_nums():
    """return a * b """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)

    return str(result)

@app.route('/div')
def div_nums():
    """divide a and b """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)

    return str(result)



operators = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div,
}

@app.route('/math/<operation>')
def do_math(operation):
    """ Do the operation between a and b parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[operation](a, b)

    return str(result)