from flask import Flask, render_template, request

app = Flask(__name__)

name_list = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']

        name_list.append(name)
        
    return render_template('index.html', name_list=name_list)

if __name__ == '__main__':
    app.run(debug=True)
