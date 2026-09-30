#파일명 app.py  => python app.py            
#                  flask run --debug --port 80   #이렇게 사용하면 if 문 추가 없이 사용가능


from flask import Flask, render_template, request
from filter import mask_comma, mask_password
from models import Member

app =Flask(__name__)
app.template_filter("mask_pw")(mask_password)
app.template_filter("comma")(mask_comma)




@app.errorhandler(404)
def errorhandler(error):
  print(error)
  return render_template('error_page.html'), 404 # 404로 넘기지 않으면 정상페이지 인식

@app.route('/', methods=['GET'])
def index():
  return render_template('2_crud/index.html')

@app.route('/join', methods=['GET','POST'])
def join():
  print(request.method)
  if request.method == 'GET':
      return render_template('2_crud/join.html') 
  elif request.method =='POST':
    # name = request.form.get('name')
    # id =request.form['id']
    # pw=request.form.get('pw')
    # addr = request.form.get('addr')
    # print(request.form.to_dict()) #post로 받은 파라미터들을 딕셔너리 형태로 받음
    try:
      member = Member(**request.form.to_dict())
    #  member = Member(name=name, id=id, pw=pw, addr=addr)
      print('가입한 회원 정보 :', member)
    except Exception as e :
      print('유효성 검사실패 {e}')
      return render_template('2_crud/join.html',
                            msg ='유효한 데이터를 입력하지 않았습니다',
                            form_data= request.form)
  return render_template('2_crud/result.html', member=member)

@app.route('/update/<name>/<id>/<pw>/<addr>', methods=['put'])
def update(name, id, pw, addr):
  return f'{name}님 의 정보가 수정되었습니다'