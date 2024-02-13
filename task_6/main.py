from flask import Flask, url_for, request

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


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1 text-align: center>Анкета претендента</h1>
                            <h2 font-size: 80% text-align: center>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input class="form-control" id="second_name" placeholder="Название фамильного клана в Clash Royal" name="second_name">
                                    <input class="form-control" id="name" placeholder="Твой ник в реальной жизни" name="name">
                                    <div>
                                        <label for="classSelect"><br></label>
                                        </div>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое образование</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>инженер-исследователь</option>
                                          <option>пилот</option>
                                          <option>строитель</option>
                                          <option>экзобиолог</option>
                                          <option>инженер по терраформированию</option>
                                          <option>климатолог</option>
                                          <option>специалист по радиационной защите</option>
                                          <option>астрогеолог</option>
                                          <option>гляциолог</option>
                                          <option>инженер жизнеобеспечения</option>
                                          <option>метеоролог</option>
                                          <option>оператор марсохода</option>
                                          <option>киберинженер</option>
                                          <option>штурман</option>
                                          <option>пилот дронов</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на марсе????????</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['second_name'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def planet_choice(planet_name):
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Моё предложение: {planet_name}</h1>
                        <div class="light alert-light" role="alert">
                      Эта планета близка к земле;</div>
                        <div class="success alert-success" role="alert">
                      На ней есть много необходимых ресурсов;</div>
                        <div class="secondary alert-secondary" role="alert">
                      На ней есть вода и атмосфера;</div>
                        <div class="warning alert-warning" role="alert">
                      На ней есть небольшое магнитное поле;</div>
                        <div class="danger alert-danger" role="alert">
                      Наконец, она просто красива!</div>
                      </body>
                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
