# SSCD Mini Project
# Grammar for Assignment Statements
# Supports: =, +=, -=, *=, /=

from flask import Flask, render_template, request

app = Flask(__name__)

input_string = ""
index = 0
error = False


def match(char):
    global index, error
    if index < len(input_string) and input_string[index] == char:
        index += 1
    else:
        error = True


def stmt():
    global index, error

    # id
    if index < len(input_string) and input_string[index].isalpha():
        index += 1
    else:
        error = True
        return

    # operator (=, +=, -=, *=, /=)
    if index < len(input_string):

        # Check for compound operators
        if input_string[index] in ['+', '-', '*', '/']:
            op = input_string[index]
            index += 1

            if index < len(input_string) and input_string[index] == '=':
                index += 1
            else:
                error = True
                return

        # Simple =
        elif input_string[index] == '=':
            index += 1
        else:
            error = True
            return
    else:
        error = True
        return

    expr()


def expr():
    global index, error
    term()

    while index < len(input_string) and input_string[index] in ['+', '-']:
        index += 1
        term()


def term():
    global index, error
    factor()

    while index < len(input_string) and input_string[index] in ['*', '/']:
        index += 1
        factor()


def factor():
    global index, error

    if index < len(input_string) and input_string[index].isalpha():
        index += 1

    elif index < len(input_string) and input_string[index].isdigit():
        index += 1

    elif index < len(input_string) and input_string[index] == '(':
        index += 1
        expr()
        match(')')

    else:
        error = True


@app.route("/", methods=["GET", "POST"])
def home():
    global input_string, index, error
    result = ""

    if request.method == "POST":
        input_string = request.form["statement"].replace(" ", "")
        index = 0
        error = False

        stmt()

        if index == len(input_string) and not error:
            result = "Valid Assignment Statement"
        else:
            result = "Invalid Assignment Statement"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
