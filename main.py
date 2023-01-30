from flask import Flask
from utilites import get_all, get_by_pk, get_by_skill


app = Flask(__name__)


@app.route('/')
def page_index():
    candidates = get_all() # Получаем кандидатов
    result = '<br>' # Перенос строки
    for candidate in candidates:
        result += candidate["name"] + '<br>'
        result += candidate["position"] + '<br>'
        result += candidate["skills"] + '<br>'
        result += '<br>'
    return f'<pre> {result} </pre>'

@app.route('/candidate/<int:pk>')
def img_candidate(pk):
    candidate = get_by_pk(pk)
    if not candidate:
        return 'Нэма кандидата'

    result = "<br>"
    result += candidate["name"] + '<br>'
    result += candidate["position"] + '<br>'
    result += candidate["skills"] + '<br>'
    result += '<br>'

    return f"""
        <img src='{candidate["picture"]}'>
        <pre> {result} </pre>"""


@app.route("/candidate/<skills>")
def get_candidates_skills(skills):
    candidates = get_by_skill(skills)
    # if not candidates:
    #     return 'Нэма кандидата'
    result = "<br>"
    for candidate in candidates:
        result += candidate["name"] + '<br>'
        result += candidate["position"] + '<br>'
        result += candidate["skills"] + '<br>'
        result += '<br>'
    return f'<pre> {result} </pre>'

if __name__ == '__main__':
    app.run(debug=True)