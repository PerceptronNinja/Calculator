from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = "0"
    if request.method == "POST":
        try:
            expression = request.form.get("expression", "0")
            result = eval(expression)  # Evaluate the mathematical expression
        except Exception:
            result = "Error"
    return render_template("calculator.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
