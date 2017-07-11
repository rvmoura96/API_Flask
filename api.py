from flask import Flask, jsonify, request, render_template
import requests
import re

app = Flask(__name__)

@app.route('/search', methods=['GET', 'POST'])

def search():
    if request.method == 'POST':
        url  = request.form['url']
        word = request.form['word']
        page = requests.get(url).text
        count = len(re.findall(word, page))

        data = {'Ocorrencias': count}
        return jsonify(data)
    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=False)