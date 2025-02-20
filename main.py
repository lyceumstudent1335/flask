from flask import Flask, url_for

COMPANY_PROMOTION = (
    "Человечество вырастает из детства.",
    "Человечеству мала одна планета.",
    "Мы сделаем обитаемыми безжизненные пока планеты.",
    "И начнем с Марса!",
    "Присоединяйся!"
)
app = Flask(__name__)


@app.route('/')
def mission():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return '</br>'.join(COMPANY_PROMOTION)


@app.route('/image_mars')
def image_mars():
    return f"""<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Привет, Марс!</title>
    </head>
    <body>
        <h1>Жди нас, Марс!</h1>
        <figure style="margin: 0;">
            <img src={url_for('static', filename='img/mars.png')}>
            <figcaption>
                Вот она какая, красная планета.
            </figcaption>
        </figure>
    </body>
</html>
"""


@app.route("/promotion_image")
def promotion_image():
    decorations_classes = (
        "text-light-emphasis bg-dark-subtle",
        "text-danger-emphasis bg-danger-subtle",
        "text-success-emphasis bg-success-subtle",
        "text-info-emphasis bg-info-subtle"
    )
    paragraphs = list()
    for i in range(len(COMPANY_PROMOTION)):
        decorations_class = decorations_classes[i] if i < len(decorations_classes) else decorations_classes[i % len(decorations_classes)]
        paragraphs.append(f'<p class="p-3 {decorations_class}"><b>{COMPANY_PROMOTION[i]}</b></p>')

    return f"""<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Колонизация</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
    </head>
    <body>
        <h1>Жди нас, Марс!</h1>
        <img src={url_for('static', filename='img/mars.png')}>
        {''.join(paragraphs)}
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    </body>
</html>
"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
