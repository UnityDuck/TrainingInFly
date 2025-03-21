from flask import Flask, render_template

app = Flask(__name__)


@app.route('/training/<prof>')
def training(prof):
    if prof.lower() == "инженер" or prof.lower() == "строитель":
        title = "Инженерные тренажёры"
        image = "first.png"
    else:
        title = "Научные симуляторы"
        image = "second.png"

    return render_template('training.html', title=title, image=image)


if __name__ == '__main__':
    app.run(debug=True)
