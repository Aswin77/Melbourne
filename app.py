from flask import Flask, request, jsonify, render_template
import abby

app = Flask(__name__)

#app = Flask(__name__)

@app.route("/")
def index():
    return render_template("app.html")

@app.route('/hello')
def hello():
    return "Hi"

@app.route('/get_location_names', methods= ['GET'])
def get_location_names():
    response = jsonify({
        'locations': abby.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_house_price', methods= ['GET','POST'])
def predict_house_price():

    suburbs = request.form['suburbs']
    bedroom2 = int(request.form['bedroom2'])
    bathroom = int(request.form['bathroom'])
    car = int(request.form['car'])
    buildingarea = float(request.form['buildingarea'])


    response = jsonify({
        'estimated_price': abby.get_estimated_price(suburbs, bedroom2, bathroom, car, buildingarea)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Python Flask server for house prediction")
    abby.load_saved_artifcats()
    app.run()

