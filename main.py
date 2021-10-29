# import "packages" from flask
from flask import Flask, render_template, request
import random
import requests
import json
import os

# create a Flask instance
app = Flask(__name__)
from algorithm.image import image_data

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render timmy.html


@app.route('/armaan/', methods=('GET', 'POST'))
def armaan():
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
            return render_template("minilabs/minilabs.html", name=name)
    # starting and empty input default
    return render_template("minilabs/minilabs.html", name="guest")

@app.route('/binary/', methods=['GET', 'POST'])
def binary():
    if request.form:
        bits = request.form.get("bits")
        try:
            if request.form.get("bulbs") == "Lizards":
                return render_template("minilabs/binary.html", bits=int(bits), bulb_on='/static/assets/lighton.png', bulb_off='/static/assets/lightoff.png')
            else:
                return render_template("minilabs/binary.html", bits=int(bits), bulb_on='/static/assets/bulbon.png', bulb_off='/static/assets/bulboff.png')
        except:
            if request.form.get("bulbs") == "Lizards":
                return render_template("minilabs/binary.html", bits=8, bulb_on='/static/assets/lighton.png', bulb_off='/static/assets/lightoff.png')
            else:
                return render_template("minilabs/binary.html", bits=8, bulb_on='/static/assets/bulbon.png', bulb_off='/static/assets/bulboff.png')
    else:
        return render_template("minilabs/binary.html", bits=8, bulb_on='/static/assets/bulbon.png', bulb_off='/static/assets/bulboff.png')

@app.route('/unicodetest/')
def unicodetest():
    return render_template("minilabs/unicodetest.html")

@app.route('/colorcodes')
def colorcodes():
    return render_template("minilabs/colorcodes.html")

@app.route('/unsignedaddition')
def unsignedaddition():
    return render_template("minilabs/unsignedaddition.html")

@app.route('/logicgates')
def logicgates():
    return render_template("minilabs/logicgates.html")

@app.route('/signedaddition/')
def signedaddition():
    return render_template("minilabs/signedaddition.html")

@app.route('/wireframe/')
def wireframe():
    return render_template("wireframe.html")

@app.route('/techtest/', methods=['GET'])
def techtest():
    return render_template("techtest.html")

@app.route('/rgb/', methods=['GET', 'POST'])
def rgb():
    return render_template('minilabs/rgb.html', images=image_data())

@app.route('/danielvar/', methods=['GET', 'POST'])
def danielvar():
    # submit button has been pushed
        var1 = request.form.get("var1")
        var2 = request.form.get("var2")
        var3 = request.form.get("var3")
        var4 = request.form.get("var4")
        var5 = request.form.get("var5")
        var6 = request.form.get("var6")
        if var1 is not None:
            average = ((int(var1) + 3) + (int(var2) + 3) + (int(var3) + 3) + (int(var4) + 3) + (int(var5) + 3) + (int(var6) + 3)) / 6
        else:
            average = 'nothing'
        return render_template("danielvar.html", var1=var1, var2=var2, var3=var3, var4=var4, var5=var5, var6=var6, average=average)

@app.route('/animalgallery/')
def animalgallery():
    return render_template("mainsite/animalgallery.html")

@app.route('/apitesting/', methods=['GET', 'POST'])
def apitesting():
    return render_template("mainsite/apitesting.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)


