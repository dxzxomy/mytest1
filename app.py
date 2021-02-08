from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from libs.pymndb import MongoDBClient


app = Flask(__name__)
bootstrap = Bootstrap(app)
ckeditor = CKEditor(app)

# csrf = CSRFProtect(app)

@app.route('/')
def index():

    mg = MongoDBClient()
    all_data = mg.all_data()


    return render_template("index.html",all_data=all_data)


if __name__ == '__main__':
    # app.run()
    app.run(debug=True, host='0.0.0.0', port=3000)
