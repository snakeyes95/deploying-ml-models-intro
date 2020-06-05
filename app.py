from flask import Flask,request
import pickle
import numpy as np 
import pandas as pd
from flasgger import Swagger
app=Flask(__name__)
swagger=Swagger(app)
@app.route('/')
def add():
    a=10
    b=20
    return str(a+b)


@app.route('/getvals')
def add_args():
    a=request.args.get('a')
    b=request.args.get('b')
    return str(int(a)+int(b))


@app.route('/getpostvals',methods=['POST'])
def add_post_args():
    a=request.form['a']
    b=request.form['b']
    return str(int(a)+int(b))


@app.route('/irisPred',methods=['GET'])
def predict():
    """Example endpoint returning a list of colors by palette
    ---
    parameters:
      - name: s_length
        in: query
        type: number
        required: True
      - name: s_width
        in: query
        type: number
        required: True
      - name: p_length
        in: query
        type: number
        required: True
      - name: p_width
        in: query
        type: number
        required: True
    """
    s_length=request.args.get('s_length')
    s_width=request.args.get('s_width')
    p_length=request.args.get('p_length')
    p_width=request.args.get('p_width')

    with open('random_forest.pkl','rb') as model_pkl:
        model=pickle.load(model_pkl)
    
    pred= model.predict(np.array([[s_length,s_width,
                    p_length,p_width]]))

    return str(pred)


@app.route('/irisPredFile',methods=['POST'])
def predict_file():
    """Example file endpoint returning a prediction of iris
    ---
    parameters:
      - name: input_file
        in: formData
        type: file
        required: true
    """
    input_data=pd.read_csv(request.files.get('input_file'),header=None)
    
    with open('random_forest.pkl','rb') as model_pkl:
        model=pickle.load(model_pkl)
    
    prediction=model.predict(input_data)
    print(prediction)
    return str(prediction)


if __name__=='__main__':
    app.run(debug=True)