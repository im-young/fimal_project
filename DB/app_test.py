from flask import Flask, render_template, url_for, request
import sqlite3

app = Flask(__name__)



@app.route('/', methods=['POST','GET'])
def user_info():
    conn = sqlite3.connect('ijm.db', isolation_level=None)
    cursor = conn.cursor()
    param = '나비'
    m = cursor.execute("SELECT * FROM wrong_test WHERE text = '%s'" % param)
        
    for x in m:
        text = x[1] # text
        right1 = x[2] #right1
        #    right2 = x[3] #right2
        #    right3 = x[4] #right3
        #     wrong = x[5] #wrong
    # Convert digital data to binary format
    with open(right1, 'wb') as file:
        img = right1.read()
    conn.commit()
    cursor.close()
    conn.close()
        
    return render_template('show2.html', text = text,img = img,right1 = right1)



if __name__ == "__main__":
    app.run(debug = True)
