from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open('model_1.pkl', 'rb'))

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

    # Validate input values
    if any(value is None for value in (a, b, c, d, e, f, g, h, i, j, k, l, m)):
        return render_template('result.html', answer="Invalid input values")

    # Convert input values to floats
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
        e = float(e)
        f = float(f)
        g = float(g)
        h = float(h)
        i = float(i)
        j = float(j)
        k = float(k)
        l = float(l)
        m = float(m)
    except ValueError:
        return render_template('result.html', answer="Invalid input values")

    userdata = np.array([[a, b, c, d, e, f, g, h, i, j, k, l, m]])
    prediction = model.predict(userdata)

    if prediction == 0:
        result_text = "Person is NOT suffering from Heart Disease"
    else:
        result_text = "Person is suffering from Heart Disease"

    return render_template('result.html', answer=result_text)

if __name__ == '__main__':
    app.run(debug=True)
