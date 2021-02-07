from flask import Flask, render_template
from flask_bootstrap import Bootstrap



app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    title = 'falsk web app'
    para = [
        "omy",
        "cali"
    ]
    return render_template("index.html", title=title, para=para)


if __name__ == '__main__':
    # app.run()
    app.run(debug=True, host='0.0.0.0', port=3000)
