from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import func, select
from flask_sqlalchemy import SQLAlchemy
from models import User, Answers, db
import sqlite3
import random
from PIL import Image, ImageOps, ImageDraw, ImageFont
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

app = Flask(__name__)  # инициализируем приложение
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///form.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
db.init_app(app)


@app.route('/questions1')
def quest1():
    return render_template('quest1.html')  # первая страница с данными о человеке


@app.route('/questions2', methods=['get'])
def quest2():
    global age, gender, education, english, langs  # сохраняем данные, введенные на прошлой странице
    if not request.args:
        return redirect(url_for('instruction'))
    age = request.args.get('age')
    gender = request.args.get('gender')
    education = request.args.get('education')
    english = request.args.get('english')
    langs = request.args.get('langs')

    with open('static/data/questions.txt', 'r', encoding='utf-8') as f:
        questext = f.read().split('\n')  # достаем вопросы
    questions = []
    for i in range(len(questext)):
        questions.append({'id': i + 1, 'text': str(i + 1) + '. ' + questext[i]})
    return render_template(
        'quest2.html',
        questions=questions
    )


@app.route('/questions3', methods=['get'])
def quest3():
    global q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, \
        q24, q25, q26, q27, q28, q29, q30, q31, q32, q33, q34, q35, q36, q37, q38, q39, q40, q41, q42

    if not request.args:
        return redirect(url_for('instruction'))  # возвращаем на главную страницу, если попали сюда не с прошлой
    q1 = request.args.get('q1')
    q2 = request.args.get('q2')
    q3 = request.args.get('q3')
    q4 = request.args.get('q4')
    q5 = request.args.get('q5')
    q6 = request.args.get('q6')
    q7 = request.args.get('q7')
    q8 = request.args.get('q8')
    q9 = request.args.get('q9')
    q10 = request.args.get('q10')
    q11 = request.args.get('q11')
    q12 = request.args.get('q12')
    q13 = request.args.get('q13')
    q14 = request.args.get('q14')
    q15 = request.args.get('q15')
    q16 = request.args.get('q16')
    q17 = request.args.get('q17')
    q18 = request.args.get('q18')
    q19 = request.args.get('q19')
    q20 = request.args.get('q20')
    q21 = request.args.get('q21')
    q22 = request.args.get('q22')
    q23 = request.args.get('q23')
    q24 = request.args.get('q24')
    q25 = request.args.get('q25')
    q26 = request.args.get('q26')
    q27 = request.args.get('q27')
    q28 = request.args.get('q28')
    q29 = request.args.get('q29')
    q30 = request.args.get('q30')
    q31 = request.args.get('q31')
    q32 = request.args.get('q32')
    q33 = request.args.get('q33')
    q34 = request.args.get('q34')
    q35 = request.args.get('q35')
    q36 = request.args.get('q36')
    q37 = request.args.get('q37')
    q38 = request.args.get('q38')
    q39 = request.args.get('q39')
    q40 = request.args.get('q40')
    q41 = request.args.get('q41')
    q42 = request.args.get('q42')
    return render_template('quest3.html')


@app.route('/results', methods=['get'])
def results():
    if not request.args:
        return redirect(url_for('instruction'))
    db.create_all()
    social = request.args.getlist('social')
    transport = request.args.getlist('transport')
    picid = request.args.get('picid')
    user = User(
        age=age,
        gender=gender,
        education=education,
        english=english,
        langs=langs,
        social=', '.join(social),
        transport=', '.join(transport),
        picid=picid
    )
    db.session.add(user)  # сохраняем данные о человеке
    db.session.commit()
    db.session.refresh(user)
    answer = Answers(id=user.id, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, q7=q7, q8=q8, q9=q9, q10=q10, q11=q11,
                     q12=q12, q13=q13, q14=q14, q15=q15, q16=q16, q17=q17, q18=q18, q19=q19, q20=q20, q21=q21, q22=q22,
                     q23=q23, q24=q24, q25=q25, q26=q26, q27=q27, q28=q28, q29=q29, q30=q30, q31=q31, q32=q32, q33=q33,
                     q34=q34, q35=q35, q36=q36, q37=q37, q38=q38, q39=q39, q40=q40, q41=q41, q42=q42)
    db.session.add(answer)  # сохраняем ответы
    db.session.commit()

    bg = Image.open(f'static/images/{picid}.jpg')  # фоновая картинка - под номером, который был выбран ползунком
    fg = Image.open(f'static/images/pic{random.randrange(1, 33)}.png')  # картинка сверху
    fg = ImageOps.contain(fg, (bg.size[0] // 2, bg.size[1] // 2))
    offset = ((bg.size[0] - fg.size[0]) // 2, (bg.size[1] - fg.size[1]) // 2)
    bg.paste(fg, offset, mask=fg)

    draw = ImageDraw.Draw(bg)
    font = ImageFont.truetype('arial', 5)  # добавляем текст
    text = random.choice(['Спасибо за прохождение опроса!', 'Вы молодец!', 'Ваш ответ для нас очень важен!',
                          'Страна вас не забудет!', 'оладушки с кленовым сиропом', 'красивая картинка'])
    tw, th = font.getbbox(text)[2] - font.getbbox(text)[0], font.getbbox(text)[3] - font.getbbox(text)[1]
    while bg.size[0] - tw >= bg.size[0] // 20:
        font.size += 1
        font = ImageFont.truetype('arial', font.size)
        tw, th = font.getbbox(text)[2] - font.getbbox(text)[0], font.getbbox(text)[3] - font.getbbox(text)[1]
        if font.size == 200:
            break
    color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
    draw.text(((bg.size[0] - tw) // 2, offset[1] + fg.size[1] + 10), text, color, font=font)
    bg.save('static/images/prize.png')  # сохраняем картинку
    return render_template('results.html')


@app.route('/stats')
def stats():
    all_info = {}
    age_stats = db.session.query(
        func.avg(User.age),
        func.min(User.age),
        func.max(User.age),
    ).one()

    #  statement = select(User.age)
    #  User.query.filter(User.id == 1).delete()
    #  db.session.commit()

    statement = select(User.age)
    print(db.session.scalars(statement).all())

    all_info['age_mean'] = age_stats[0]
    all_info['age_min'] = age_stats[1]
    all_info['age_max'] = age_stats[2]
    all_info['total_count'] = User.query.count()  # собираем статистику
    on_bus = db.session.query(Answers.q8).filter(User.id == Answers.id).filter(Answers.q8.like('на'))\
        .filter(User.transport.contains('bus')).all()  # в хтмл описано, что это за статистика
    in_bus = db.session.query(Answers.q8).filter(User.id == Answers.id).filter(Answers.q8.like('в'))\
        .filter(User.transport.contains('bus')).all()
    on_nobus = db.session.query(Answers.q8).filter(User.id == Answers.id).filter(Answers.q8.like('на'))\
        .filter(~User.transport.contains('bus')).all()
    in_nobus = db.session.query(Answers.q8).filter(User.id == Answers.id).filter(Answers.q8.like('в'))\
        .filter(~User.transport.contains('bus')).all()
    q11_answers = db.session.query(Answers.q11)
    labels, values = zip(*Counter(q11_answers).items())

    indexes = np.arange(len(labels))

    plt.bar(indexes, values)
    plt.xticks(indexes, labels)
    plt.savefig('static/images/stats.png')  # сохраняем график
    return render_template('stats.html', all_info=all_info, on_bus=len(on_bus), in_bus=len(in_bus),
                           on_nobus=len(on_nobus), in_nobus=len(in_nobus))


@app.route("/")
def instruction():
    return render_template('index.html')


if __name__ == '__main__':  # запускаем программу
    app.run(debug=False)
