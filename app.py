from flask import Flask, render_template, request, redirect, url_for, flash
from models import Question, db, User
from config import Config
import random
from flask_login import LoginManager, login_user, login_required, current_user, logout_user

app = Flask(__name__)
app.config.from_object(Config)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
db.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']

        if User.query.filter_by(email=email).first():
            flash('Email đã tồn tại. Vui lòng chọn email khác.', 'danger')
            return redirect(url_for('register'))

        new_user = User(
            username=username,
            email=email,
            password=password,
            role=role
            )
        db.session.add(new_user)
        db.session.commit()
        flash('Đăng ký thành công! Bạn có thể đăng nhập.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            login_user(user)
            flash('Đăng nhập thành công!', 'success')
            return redirect(url_for('add_question'))
        else:
            flash('Đăng nhập thất bại. Vui lòng kiểm tra lại thông tin.', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Bạn đã đăng xuất thành công!', 'success')
    return redirect(url_for('login'))


@app.route("/add_question", methods=["GET", "POST"])
@login_required
def add_question():
 if current_user.role != 'teacher':
  flash('Bạn không có quyền truy cập!', 'danger')   
  return redirect(url_for('view_questions'))
  
 if request.method == "POST":
  question_text = request.form.get('question_text')
  choices = request.form.get('choices')
  correct_answer = request.form.get('correct_answer')
  difficulty_level = request.form.get('difficulty_level')
  category = request.form.get('category')
 
  new_question = Question(
   question_text=question_text,
   choices=choices,
   correct_answer=correct_answer,
   difficulty_level=difficulty_level,
   category=category
  )
  db.session.add(new_question)
  db.session.commit()
  flash('Câu hỏi đã được thêm thành công!', 'success')
  return redirect(url_for('view_questions'))
 return render_template('add_question.html')

@app.route("/view_questions", methods=["GET"])
def view_questions():
    difficulty_level = request.args.get('difficulty_level')
    if difficulty_level:
        questions = Question.query.filter_by(difficulty_level=difficulty_level).all()
    else:
        questions = Question.query.all()
    return render_template('view_questions.html', questions=questions)


@app.route("/generate_exam", methods=["GET", "POST"])
@login_required
def generate_exam():
 if current_user.role != 'teacher':
  flash('Bạn không có quyền truy cập!', 'danger')   
  return redirect(url_for('view_questions'))
 
 if request.method == "POST":
  num_questions = int(request.form.get('num_questions'))
  difficulty_level = request.form.get('difficulty_level')
  questions = Question.query.filter_by(difficulty_level=difficulty_level).all()
  selected_questions = random.sample(questions, num_questions)
  return render_template('exam.html', questions=selected_questions)
 return render_template('generate_exam.html')

@app.route("/generate_exam_clo", methods=["GET", "POST"])
@login_required
def generate_exam_clo():
 if current_user.role != 'teacher':
  flash('Bạn không có quyền truy cập!', 'danger')   
  return redirect(url_for('view_questions'))
    
 if request.method == "POST":
  num_questions_clo1 = int(request.form.get('num_questions_clo1'))
  num_questions_clo2 = int(request.form.get('num_questions_clo2'))
  CLO1 = request.form.get('CLO.1')
  CLO2 = request.form.get('CLO.2')
  questions_clo1 = Question.query.filter_by(category=CLO1).all()
  questions_clo2 = Question.query.filter_by(category=CLO2).all()
  selected_questions_clo1 = random.sample(questions_clo1, num_questions_clo1)
  selected_questions_clo2 = random.sample(questions_clo2, num_questions_clo2)
  final_questions = selected_questions_clo1 + selected_questions_clo2
  return render_template('exam.html', questions=final_questions)
 return render_template('generate_exam_clo.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
