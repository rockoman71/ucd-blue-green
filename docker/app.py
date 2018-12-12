from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<html><head>" \
           "<title>IBM Demo DevOps</title></head>" \
           "<body style='background-color:{backgroundcolor};'>" \
           "<p><font size='10'>IBM DevOps Demo - UrbanCode Deploy & IBM Cloud Private!!<br/></font></p>" \
           "<p><font size='6'>Hello {name}!<br/></font></p>" \
           "<p><font size='6'><b>Hostname:</b> {hostname}<br/></font></p>" \
           "<p><font size='6'><b>Environment:</b> {env}<br/></font></p>" \
           "<p><font size='6'><b>Version:</b> {version}<br/></font></p>" \
           "</body></html>"
    return html.format(name=os.getenv("NAME", "world"), 
                       hostname=socket.gethostname(), 
                       env=os.getenv("env", "Dev"), 
                       backgroundcolor=os.getenv("backgroundcolor", "MintCream"),
                       version=os.getenv("version", "n/a"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
