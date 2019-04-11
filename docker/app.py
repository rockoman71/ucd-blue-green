from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<html><head>" \
           "<title>IBM Cloud Private + dev/test/delivery POT</title></head>" \
           "<body style='background-color:{backgroundcolor};'>" \
           "<p><font size='6'>IBM DevOps PoT - Transformation Advisor, Microclimate, UrbanCode Deploy & Velocity<br/></font></p>" \
           "<!--<br><font size='5'><a target='_blank' rel='noopener' href='http://conf.bluedemos.com/app/home/session/3834/7o7mdu0zli69U8ZCBTKKFWZ1UV7HZSY80hiwmolqohwfkw341k7eel6dun23gjs8'>Click here to open your DevOps ICP PoT environment</a></font><br>-->" \
           "<p><font size='4'><b>Hostname:</b> {hostname}<br/></font></p>" \
           "<p><font size='4'><b>Environment:</b> {env}<br/></font></p>" \
           "<p><font size='4'><b>Version:</b> {version}<br/></font></p>" \
           "</body></html>"
    return html.format(name=os.getenv("NAME", "world"), 
                       hostname=socket.gethostname(), 
                       env=os.getenv("env", "Dev"), 
                       backgroundcolor=os.getenv("backgroundcolor", "MintCream"),
                       version=os.getenv("version", "n/a"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
