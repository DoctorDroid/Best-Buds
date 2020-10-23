from flask import Flask, render_template, request, jsonify

#from (the request file) import *
# TODO the request file
#import logging
import requests
#import string

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return "Honestly, Bessie? People dont care about anyone but themselves. They dont notice anything. They are never looking at whats interesting. Theyre always looking at themselves. -Kevin Wilson, Nothing to See Here "


    @app.route('/predict', methods=['POST'])
    def model1(input_string):
        # Requested to return Name, Type, and Description
        stringData = requests.values['stringData']
        user_input = pd.DataFrame([word.strip(string.punctuation) for word in input_string.split()], 
                                    columns=['search_string']) # string separated by comma to single column df
        MJ= marijuana.copy()
        MJ['fitness'] = 0 ## sets all strains initial fitness to 0
        for i in range(len(MJ)):
            for each_string in user_input['search_string']:
                if each_string in MJ['Ailment'][i]:
                    MJ['fitness'][i] +=1
                if each_string in MJ['Effects_x'][i]:
                    MJ['fitness'][i] +=1
                if each_string in MJ['Effects_y'][i]:
                    MJ['fitness'][i] +=1
        df = MJ.nlargest(20, 'fitness')
        return df.to_json(orient="records") # as is this will return a df with the top 20 matches. May need to adjust.

    # df_pred = model1(StringData)
    # '''TODO for loop to extract info to return from each strain
    #         strain = 
    #         profile = 
    #         ...other fields to return'''
    # return jsonify({'Strain':strain, 'Indica_Sativa_Hybrid':indica_sativa_hybrid, 'Description':description}) #this may need adjustments
    return app
