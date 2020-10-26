from flask import Flask, request, jsonify
import pandas as pd
import string
from flask_cors import CORS, cross_origin
import json


def create_app():
    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    @app.route('/')
    @cross_origin()
    def root():
        return "Honestly, Bessie? People dont care about anyone but themselves. They dont notice anything. They are never looking at whats interesting. Theyre always looking at themselves. -Kevin Wilson, Nothing to See Here "


    @app.route('/predict', methods=['GET', 'POST'])
    def model1():
        marijuana = pd.read_csv("https://raw.githubusercontent.com/Build-Week-PT-Med-Cabinet-2/DS/main/Marijuana.csv")
        
        request_json = request.get_json()
        Type = request_json['Type']
        Depression = request_json['Depression']
        Inflammation = request_json['Inflammation']
        Insomnia = request_json['Insomnia']
        Appetite = request_json['Appetite']
        Pain = request_json['Pain']
        Nausea = request_json['Nausea']
        Creative = request_json['Creative']
        Energetic = request_json['Energetic']
        Euphoric = request_json['Euphoric']
        Focused = request_json['Focused']
        Happy = request_json['Happy']
        Hungry = request_json['Hungry']
        Relaxed = request_json['Relaxed']
        
        stringData = [Type, Depression, Inflammation, Insomnia, 
                      Appetite, Pain,Nausea, Creative, Energetic, 
                      Euphoric,Focused, Happy, Hungry, Relaxed]
        
        user_input = pd.DataFrame(stringData, columns=['search_string']) # string separated by comma to single column df
        
        MJ= marijuana.copy()
        if Type.lower() == 'sativa':
            MJ = MJ[MJ['Type'] == 'sativa']
        elif Type.lower() == 'indica':
            MJ = MJ[MJ['Type'] == 'indica']
        elif Type.lower() == 'hybrid':
            MJ = MJ[MJ['Type'] == 'hybrid']
        else : 
            pass
        
        
        MJ['fitness'] = 0 ## sets all strains initial 'fitness' to 0
        for i in range(len(MJ)):
            for each_string in user_input['search_string']:
                if each_string in MJ['Ailment'][i]:
                    MJ['fitness'][i] +=1
                if each_string in MJ['Effects_x'][i]:
                    MJ['fitness'][i] +=1
                if each_string in MJ['Effects_y'][i]:
                    MJ['fitness'][i] +=1
        
        df = MJ.nlargest(20, 'fitness')
        df = df.drop(columns=['id','Unnamed: 0', 'fitness'], axis=1)
        results = df.to_json(orient="records")
        return results # this will return a df with the top 20 matches,
                       # filtered by type, as a JSON object, without ID key. 
    return app