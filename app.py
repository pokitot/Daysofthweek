from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_day', methods=['POST'])
def get_day():
    import datetime

    date_str = request.form['date']
    date_obj = datetime.datetime.strptime(date_str, '%m/%d/%Y')
    day_of_week = date_obj.strftime('%A')

    return day_of_week

if __name__ == '__main__':
    app.run(debug=True)
