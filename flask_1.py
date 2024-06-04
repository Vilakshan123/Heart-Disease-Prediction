from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open('model_1.pkl', 'rb'))
# logistic = pickle.load(open('logistic.pkl','rb'))

@app.route('/')
def home():
    return render_template('Index.html')

@app.route('/result', methods=['POST'])
def result():
    a = request.form.get('Age')
    b = request.form.get('Sex')
    c = request.form.get('CP')
    d = request.form.get('TrestBPS')
    e = request.form.get('chol')
    f = request.form.get('fbs')
    g = request.form.get('restECG')
    h = request.form.get('thalach')
    i = request.form.get('exang')
    j = request.form.get('oldpeak')
    k = request.form.get('slope')
    l = request.form.get('ca')
    m = request.form.get('thal')

    userdata = (a, b, c, d, e, f, g, h, i, j, k, l, m)
    userarray = np.asarray(userdata)
    reshaped = userarray.reshape(1, -1)
    prediction = model.predict(reshaped)

    if prediction == 0:
        result_text = "Person is NOT suffering from Heart Disease"
    else:
        result_text = "Person is suffering from Heart Disease"

    return render_template('result.html', answer=result_text)

if __name__ == '__main__':
    app.run(debug=True)

