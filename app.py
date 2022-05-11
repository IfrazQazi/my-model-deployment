from flask import Flask , render_template , request

import decision_tree as dt



app = Flask(__name__)

@app.route('/')
def home():
    flower_pred = ''
    return render_template('first.html',**locals())


@app.route('/predict', methods =['GET','POST'])
def first():


    sepal_length_  = float(request.form['sepal_length_'])
    sepal_width_  = float(request.form['sepal_width_'])
    petal_length_  = float(request.form['petal_length_'])
        
    petal_width_  = float(request.form['petal_width_'])
    flower_pred = dt.flower(sepal_length_, sepal_width_, petal_length_, petal_width_)
    
        
    return render_template('first.html', **locals())
    # pass
# @app.route('/second')
# def second():
#     return render_template('index.html')

if __name__ =='__main__':
    app.run(debug=True)