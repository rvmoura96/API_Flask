from flask import Flask, request, render_template
import requests
import re
import json

app = Flask(__name__)

def count(url, word):
    page = requests.get(url).text
    contador = len(re.findall(word, page))
    data = {"Ocorrencias": contador}
    return json.dumps(data)
    
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        url  = request.form['url']
        word = request.form['word']        
        return count(url, word)

    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=False)