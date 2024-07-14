from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")
 
@app.route('/tarun')
def tarun():
   return render_template("tarun.html")

if __name__=="__main__":
    app.run(debug=True,port=33)