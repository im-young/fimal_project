from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
#import sqlite3 as sql
import os
import random
import sqlite3



app = Flask(__name__)

#globla 변수
count = 0
test_class = ['나비','지렁이','컴퓨터','next']
# 밑에 next를 안 넣고 coutn>=3 을 하면 오류남 (인덱스 에러)/ 왜인진 모르겠지만 맨 마지막 인덱스는 안 나온다.
OX =[] # db 저장용 
# html 렌더링
@app.route('/',  methods=['POST','GET'])

def wrong_img():
    
    global count
    # 변수에 이미지 이름 넣기
    global test_class
    img1 =test_class[0] + '1'
    img2=test_class[0] + '2'
    img3= test_class[0] + '3'
    img4= test_class[0] + 'X'
    # 랜덤으로 텍스트 보내기
    random_class =[img1,img2,img3,img4 ]
    random.shuffle(random_class)
    img1 = random_class[0]
    img2 = random_class[1]
    img3 = random_class[2]
    img4 = random_class[3]
    
    # 처음엔 for문으로 작성하려고 했으나 렌더링 될 때는 마지막 것만 되기 때문에 필요가 없음    
    # for i in test_class :   
    #     # str = test_class[i]    
    #     random_list = [i+'1', i+'2',i+'3',i+'X']
    #     random_list_2 = []
    #     random.shuffle(random_list)
    #     for  j in random_list:
    #         random_list_2.append(j)
    #     img1 = random_list_2[0]
    #     img2 = random_list_2[1]
    #     img3 = random_list_2[2]
    #     img4 = random_list_2[3]
        
    # 누른 버튼의 text 를 받아서 정답인지 오답인지 판별하기
    global OX
    if request.method == 'POST':
        image = str(request.form['button'])
        if 'X' in image:
            OX.append('정답')
        else: OX.append('오답')
        
    count += 1 
    test_class.remove(test_class[0])
    
    if count >=4 :
        return redirect(url_for('end')) # redirect를 할때는 route 옆에 오는 글자를 넣어줘야함(함수이름이 아님)
    else: 
        return render_template('4th_test.html',img1 = img1, img2=img2,img3=img3,img4=img4) 
   

@app.route('/end',  methods=['POST','GET'])
def end():
    # DB 저장 
    conn = sqlite3.connect('ijm.db', isolation_level=None)
    # 커서
    cursor = conn.cursor()
    # 테이블 생성(데이터 타입 = TEST, NUMERIC, INTEGER, REAL, BLOB(image) 등)
    # 필드명(ex. name) -> 데이터 타입(ex. text) 순서로 입력 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS wrong_test (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        game text,
        OX1 text,
        OX2 text,
        OX3 text)""")
    
    # db 에 정보 저장
    game = '틀린그림찾기'
    OX1 = OX[0]
    OX2 = OX[1]
    OX3 = OX[2]
    
    cursor.execute("""
        INSERT INTO wrong_test (game, OX1,OX2,OX3) VALUES (?,?,?,?)          
        """, (game, OX1,OX2,OX3)
        )
    conn.commit()
    cursor.close()
    conn.close() 
    return render_template('4-2_test.html')
    
if __name__ == '__main__':
    app.run( debug=True)  