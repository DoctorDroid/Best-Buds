from flask import Flask, render_template, request, jsonify
from (the request file) import *
# TODO the request file
import logging
import requests



app = Flask(__name__)

@app.route('/')

def root():
    pass


@app.route('/predict', methods=['POST'])

    # Requested to return Name, Type, and Description
    json_req = request.get_json()
    # TODO find which variables are inbound
    effects = json_req['effects']
    ailments = json_req['ailments']
    # input_variable3 = request_json['input_variable3'] *** I don't believe there is a third, but just in case.
    # string separated by comma to list

    # TODO I left this commented out because I don't believe we are required to log?
    # url = "https://cannedmedical.herokuapp.com/recommendation/search" (wrong anyway)
    # logging.info(url)
    payload = {"user_id": user_id,   <<<---- the payload will be the input variables
               "Prediction": pred}   <<<---- whatever we get from above
    # logging.info(payload)
    # req_log = requests.post(url, json=payload)
    # logging.info("status_code: " + str(req_log.status_code))

    # TODO ensure variables are correct for return
    # If they want conditions treated, how should we handle that?  Should we work on combining the two, or deliver one?
    return jsonify({'Strain':strain, 'Indica_Sativa_Hybrid':indica_sativa_hybrid, 'Description':description})

if __name__ == '__main__':
    app.run()