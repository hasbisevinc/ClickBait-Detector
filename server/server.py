from flask import Flask, request
from flask_cors import CORS
import feature as ft
import knn
app = Flask(__name__, static_url_path='')
CORS(app)

clf = knn.init()


@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route("/classify.ai", methods=["POST"])
def classify():
    title = request.form["title"]
    body = request.form["body"]
    if len(title) < 3 or len(body) < 3:
        return "-1"
    features = ft.getFeatures(str(title), str(body))
    result = knn.test(clf, features)
    return str(result[0])

if __name__ == '__main__':
  app.run(debug=True)
