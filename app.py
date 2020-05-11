from flask import Flask,request


app=Flask(__name__)

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

if __name__=='__main__':
    app.run(debug=True)