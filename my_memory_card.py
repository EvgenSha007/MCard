from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import * 

app = QApplication([])
win = QWidget()
win.resize(400, 300)

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def click_OK():
    if btn.text() == 'Ответить':
        check_answer() 
    else:
        next_question()

def next_question():
    win.total += 1
    print('Статистика\n-Всего вопросов: ', win.total, '\n-Правильных ответов: ', win.score)
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q) 

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        win.score += 1
        print('Статистика\n-Всего вопросов: ', win.total, '\n-Правильных ответов: ', win.score)
        print('Рейтинг: ', (win.score/win.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг: ', (win.score/win.total*100), '%')

def ask(q: Question):
    shuffle(answers) 
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    qwe.setText(q.question) 
    lb_Correct.setText(q.right_answer) 
    show_question()

def show_correct(x):
    rigth.setText(x)
    show_result()

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn.setText('Ответить')
    RadioGroup.setExclusive(False) 
    but1.setChecked(False)
    but2.setChecked(False)
    but3.setChecked(False)
    but4.setChecked(False)
    RadioGroup.setExclusive(True) 

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn.setText('Следующий вопрос')






win.score = 0
win.total = 0

questions_list = [] 
questions_list.append(Question('Самый большой вулкан Солнечной системы называется «Гора Олимп». Где он находится?', 'Марс', 'Венера ', 'Земля ', 'Юпитер'))
questions_list.append(Question('Большое красное пятно на Юпитере, что это?', 'буря ', 'кратер', 'озеро', 'вулкан '))
questions_list.append(Question('Из чего в основном состоит Солнце?', 'газ ', 'расплавленный метал', 'жидкая лава', 'камень'))
questions_list.append(Question('Из чего в основном состоят кометы?', 'лед и пыль ', 'ржавый металл', 'расплавленный камень', 'ядовитая жидкость '))
questions_list.append(Question('Где находится пояс астероидов?', 'Марсом и Юпитером', 'Землей и Марсом', 'Юпитером и Сатурном', 'Землей и Венерой'))

btn = QPushButton('Ответить') 
qwe = QLabel('Текст вопроса') 

RadioGroupBox = QGroupBox("Варианты ответов") 
but1 = QRadioButton('Вариант 1')
but2 = QRadioButton('Вариант 2')
but3 = QRadioButton('Вариант 3')
but4 = QRadioButton('Вариант 4')
answers = [but1, but2, but3, but4]

RadioGroup = QButtonGroup() 
RadioGroup.addButton(but1)
RadioGroup.addButton(but2)
RadioGroup.addButton(but3)
RadioGroup.addButton(but4)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(but1) 
layout_ans2.addWidget(but2)
layout_ans3.addWidget(but3) 
layout_ans3.addWidget(but4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 

RadioGroupBox.setLayout(layout_ans1) 

AnsGroupBox = QGroupBox("Результат теста")
rigth = QLabel('Верно или нет') 
lb_Correct = QLabel('Правильный ответ')

layout_res = QVBoxLayout()
layout_res.addWidget(rigth, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 


layout_line1.addWidget(qwe, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()

layout_line3.addWidget(btn, stretch=2) 
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addLayout(layout_line3, stretch=1)


win.setLayout(layout_card)

btn.clicked.connect(click_OK)

next_question()
win.show()
app.exec()
