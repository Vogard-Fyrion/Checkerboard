from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        "index.html", 
        x = 8, 
        y = 8,
        colorful1 = False,
        colorful2 = False)

@app.route('/<int:x>')
def x_count(x):
    return render_template(
        "index.html", 
        x = x, 
        y = 8,
        colorful1 = False,
        colorful2 = False)

@app.route('/<int:x>/<int:y>')
def area_count(x,y):
    return render_template(
        "index.html", 
        x = x, 
        y = y,
        colorful1 = False,
        colorful2 = False)


@app.route('/<int:x>/<int:y>/<color1>')
def color1(x,y,color1):
    return render_template(
        "index.html", 
        x = x, 
        y = y, 
        color1 = color1, 
        colorful1 = True, 
        colorful2 = False)

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def color_2(x,y,color1,color2):
    return render_template(
        "index.html", 
        x = x, 
        y = y, 
        color1 = color1,
        color2 = color2,
        colorful1 = True, 
        colorful2 = True)

if __name__ == "__main__":
    app.run(debug = True)