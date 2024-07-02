from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "lukmans_aderwj234575"


@app.route('/')
def home():
    #flash("What's your name?")
    return render_template('index.html')

#
# @app.route('/greet')
# def greet():
#     flash("Hi " + str(request.form['name_input']) + ", Glad to meet you")
#     return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=8080)