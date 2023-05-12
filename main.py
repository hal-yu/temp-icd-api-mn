from flask import Flask, request 
import pandas as pd 

df = pd.read_csv('./data/Drugs.csv')

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return 'this is a API service for drug details'

@app.route('/preview', methods=["GET"])
def preview():
    top10rows = df.head(10)
    result = top10rows.to_json(orient="records")
    return result

@app.route('/drugs/<value>/<value2>', methods=['GET'])
def icdcode(value, value2):
    print('value: ', value)
    print('value: ', value2)    
    filtered = pd.DataFrame()
    if value == 'dose':
        filtered = df[df['DOSAGE_FORM'] == value2]
    elif value == 'name':
        filtered = df[df['NPROPNAME'] == value2]
    elif value == 'year':
        filtered = df[df['LAUNCH_YEAR'] == int(value2)]
    if len(filtered) <= 0:
        return 'This does not exist D:'
    else: 
        return filtered.to_json(orient="records")

@app.route('/drugs/<value>/dose/<value2>')
def icdcode2(value, value2):
    filtered = df[df['NPROPNAME'] == value]
    filtered2 = filtered[filtered['DOSAGE_FORM'] == value2]
    if len(filtered2) <= 0:
        return 'This does not exist D:'
    else: 
        return filtered2.to_json(orient="records")    
    

if __name__ == '__main__':
    app.run(debug=True)