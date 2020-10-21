from flask import Flask, render_template, request, jsonify

#from (the request file) import *
# TODO the request file
#import logging
import requests
import string


app = Flask(__name__)

@app.route('/')

def root():
    pass


@app.route('/predict', methods=['POST'])

    # Requested to return Name, Type, and Description
    json_req = request.get_json()
    # TODO find which variables are inbound
    # effects = json_req['effects']
    # ailments = json_req['ailments']
    # input_variable3 = request_json['input_variable3'] *** I don't believe there is a third, but just in case.

    stringData = json_req['stringData']

    def model1(input_string):
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
            return MJ.nlargest(20, 'fitness') # as is this will return a df with the top 20 matches. May need to adjust.

    df_pred = model1(StringData)
    '''TODO for loop to extract info to return from each strain
            strain = 
            profile = 
            ...other fields to return'''
    return jsonify({'Strain':strain, 'Indica_Sativa_Hybrid':indica_sativa_hybrid, 'Description':description}) #this may need adjustments

if __name__ == '__main__':
    app.run()