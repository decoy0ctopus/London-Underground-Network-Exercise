
from urllib import request
import json

from flask import Flask, jsonify, render_template
from flask import request as flask_request

from network.path import PathFinder
from tube.map import TubeMap

application = Flask(__name__)

@application.route('/')
def my_form():
    return render_template('index.html')

def get_model():
    tubemap = TubeMap()
    tubemap.import_from_json("data/london.json")
    


@application.route("/predict", methods=["POST"])
def predict():
    print("predict")
    tubemap = TubeMap()
    tubemap.import_from_json("data/london.json")
    path_finder = PathFinder(tubemap)
    stations = json.loads(flask_request.get_data(as_text=True))
    stations = path_finder.get_shortest_path(stations['start_station'], stations['end_station'])
    station_names = str([station.name for station in stations])
    response = {
        'prediction': {
            'confidence': station_names
        }
    }
    return jsonify(response)

if __name__ == "__main__":
    get_model()

    # start flask app
    application.run(host='0.0.0.0', port ='5002')    