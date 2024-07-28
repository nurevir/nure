from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hundre_spm')
def hundre_spm():
    return render_template('hundre_spm.html')

@app.route('/kalas_drikkelek')
def kalas_drikkelek():
    return render_template('kalas_drikkelek.html')

@app.route('/jeg_har_aldri')
def jeg_har_aldri():
    return render_template('jeg_har_aldri.html')


@app.route('/karaoke')
def karaoke():
    return render_template('karaoke.html')

@app.route('/karaoke/mamma_mia')
def mamma_mia():
    return render_template('mamma_mia.html')

@app.route('/karaoke/freddy_kalas')
def freddy_kalas():
    return render_template('freddy_kalas.html')

@app.route('/karaoke/jenter')
def jenter():
    return render_template('jenter.html')

@app.route('/karaoke/forever_alone')
def forever_alone():
    return render_template('forever_alone.html')

@app.route('/karaoke/lekker')
def lekker():
    return render_template('lekker.html')


@app.route('/truth_or_drink')
def truth_or_drink():
    return render_template('truth_or_drink.html')

@app.route('/do_or_drink')
def do_or_drink():
    return render_template('do_or_drink.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

