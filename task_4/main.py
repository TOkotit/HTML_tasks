from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def mission():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promo():
    return ('Человечество вырастает из детства.<br><br>Человечеству мала одна планета.'
            '<br><br>Мы сделаем обитаемыми безжизненные пока планеты.<br><br>И начнем с Марса!<br><br>Присоединяйся!')


@app.route('/image_mars')
def mars():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/MARS.png')}" width="500" height="500"  
           alt="здесь должна была быть картинка, но не нашлась">
                        <h1>Вот она какая, красная планета</h1>
                      </body>
                    </html>"""


@app.route('/promotion_image')
def promo_img():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1 style="color: red">Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/MARS.png')}" width="400" height="400"
           alt="здесь должна была быть картинка, но не нашлась">
                        <div class="dark alert-dark" role="alert">
                      Человечество вырастает из детства.</div>
                        <div class="success alert-success" role="alert">
                      Человечеству мала одна планета.</div>
                        <div class="secondary alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.</div>
                        <div class="warning alert-warning" role="alert">
                      И начнем с Марса!</div>
                        <div class="danger alert-danger" role="alert">
                      Присоединяйся!</div>
                      </body>
                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
