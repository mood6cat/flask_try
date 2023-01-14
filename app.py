from flask import Flask
import json
import utilites


app = Flask(__name__)


@app.route('/')
def page_index():
    candidates = utilites.get_all() # Получаем кандидатов
    result = '<br>' # Перенос строки
    for candidate in candidates:
        result += candidate["name"] + '<br>'
        result += candidate["position"] + '<br>'
        result += candidate["skills"] + '<br>'
        result += '<br>'
    return f'"<pre>"{result}"</pre>"'






# @app.route("/")
# def page_index():
#     return "Главная страничка"
# @app.route("/profile/")
# def page_profile():
#     return "Профиль пользователя"
# @app.route("/messages/")
# def page_messages():
#     return "Сообщения пользователя"
# # Для этого достаточно чуть-чуть дописать вьюшку
#
# @app.route('/users/<uid>')
# def profile(uid):
#     return f'<h1>Профиль {uid}</h1>'
#
# @app.route('/catalog/items/<itemid>')
# def profil(itemid):
#     return f'<h1>Страничка товара {itemid}</h1>'
