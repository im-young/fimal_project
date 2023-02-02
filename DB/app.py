from flask import Flask, render_template, url_for, request
import sqlite3

app = Flask(__name__)


# static(폴더)에 이미지를 미리 저장한 후 텍스트만 불러오는 작업(이미지는 html에서 불러옴)
@app.route('/', methods=['POST','GET'])
def wrong_img():
        conn = sqlite3.connect('ijm.db', isolation_level=None)
        cursor = conn.cursor()
        param = '나비'
        m = cursor.execute("SELECT * FROM wrong_test WHERE text = '%s'" % param)
        
        for x in m:
            text = x[1] # text
            right1 = x[2] #right1
        #     right2 = x[3] #right2
        #     right3 = x[4] #right3
        #     wrong = x[5] #wrong
        
    
        # 이미지를 저장해서 불러오는 작업이면 여기서 해야하지만 미리 저장되어 있는 이미지를 불러와도 되는 상황이라 굳이 이 작업을 하지 않아도 될거 같다.   
        # with open('C:\\Users\\admin\\Desktop\\worng_test\\static\\img\\나비1.PNG', 'wb') as f:
        #     f.write(right1)
        # with open('C:\\Users\\admin\\Desktop\\worng_test\\static\\img\\나비2.PNG', 'wb') as f:
        #     f.write(right2)
        # with open('C:\\Users\\admin\\Desktop\\worng_test\\static\\img\\나비3.PNG', 'wb') as f:
        #     f.write(right3)
        # with open('C:\\Users\\admin\\Desktop\\worng_test\\static\\img\\나비X.PNG', 'wb') as f:
        #     f.write(wrong)
    
            
        conn.commit()
        cursor.close()
        conn.close()
        
        return render_template('show.html',text = text, right1=right1)


if __name__ == "__main__":
    app.run(debug = True)
