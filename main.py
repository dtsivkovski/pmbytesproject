# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render timmy.html
@app.route('/timmy/')
def kangaroos():
    return render_template("timmy.html")


@app.route('/armaan/', methods=('GET', 'POST'))
def walruses():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("armaan.html", name=name)
    # starting and empty input default
    return render_template("armaan.html", name="guest")
    return render_template("armaan.html")


@app.route('/chris/')
def hawkers():
    return render_template("chris.html")


@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.route('/daniel/', methods=('GET', 'POST'))
def daniel():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("daniel.html", name=name)
    # starting and empty input default
    return render_template("daniel.html", name="guest")

@app.route('/timmy/', methods=('GET', 'POST'))
def timmy():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("timmy.html", name=name)
    # starting and empty input default
    return render_template("timmy.html", name="guest")

@app.route('/about-us/')
def aboutus():
    return render_template("about-us.html")

@app.route('/minilabs/', methods=['GET', 'POST'])
def minilabs():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("minilabs.html", name=name)
    # starting and empty input default
    return render_template("minilabs.html", name="guest")

@app.route('/binary/')
def binary():
    return render_template("binary.html")

@app.route('/wireframe/')
def wireframe():
    return render_template("wireframe.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
