from flask import Flask, render_template, jsonify, redirect
import subprocess
import json
import os
from pro_ai_module import generate_gemini_ending

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('programfinalproject/start.html')
@app.route('/surguide')
def guide():
    return render_template('programfinalproject/surguide.html')

@app.route('/setting')
def setting():
    return render_template('programfinalproject/settingmenu.html')

@app.route('/aboutus')
def aboutus():
    return render_template('programfinalproject/aboutus.html')

@app.route('/privacy')
def privacy():
    return render_template('programfinalproject/privacpolicy.html')

@app.route('/design')
def design():
    return render_template('programfinalproject/desgind.html')



import subprocess
import sys
@app.route('/start_game')
def start_game():
    try:
        log_file = open("log.txt", "w")
        if sys.platform.startswith('win'):
            # Windows: 透過 cmd 前台開視窗
            subprocess.Popen([ "python", "main.py"], shell=True, stdout=log_file, stderr=log_file)
        elif sys.platform.startswith('darwin'):
            # macOS: 透過 Terminal.app 啟動
            subprocess.Popen(["open", "-a", "Terminal", "python3 main.py"], stdout=log_file, stderr=log_file)
        else:
            # Linux: 普通方式啟動
            subprocess.Popen(["python3", "main.py"], stdout=log_file, stderr=log_file)
        return "<h3>遊戲啟動中，請查看你的桌面是否有彈跳出遊戲視窗。</h3><p>若沒看到視窗，請檢查 <code>log.txt</code> 或按 Alt+Tab。</p>"
        #return redirect('/final')
    except Exception as e:
        return f"<h3>遊戲啟動失敗：</h3><pre>{str(e)}</pre>"
        


@app.route('/final')
def show_final():
    result_data = {}
    if os.path.exists("result.json"):
        with open("result.json", "r", encoding="utf-8") as f:
            result_data = json.load(f)
    else:
        result_data = {
            "progress": 0,
            "health": 0,
            "energy": 0,
            "graphData": {
                "labels": [], "grades": [], "healths": [], "energys": []
            }
        }
    if result_data["progress"] >= 100:
        status = "success"
    else:
        status = "fail"  

    ending_text = generate_gemini_ending(
        result_data["progress"],
        result_data["health"],
        result_data["energy"],
        result_data["ending1"]
    )
    return render_template('programfinalproject/finaltheend.html', data=json.dumps(result_data), ending=result_data["ending1"], ending2=ending_text, status=status)


if __name__ == '__main__':
    app.run(debug=True)
