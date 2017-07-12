import json
import api

def test_count1():
    data = api.count('https://pt.wikipedia.org/wiki/Sons_of_Anarchy', 'Gemma')
    compara = '{"Ocorrencias": 4}'
    json.dumps(compara)
    assert data == compara
    
def test_count2():
    data = api.count('http://pythonclub.com.br/what-the-flask-pt-1-introducao-ao-desenvolvimento-web-com-python.html#template_com_jinja_2', 'quokka')
    compara = '{"Ocorrencias": 2}'
    json.dumps(compara)
    assert data == compara

def test_count3():
    data = api.count('https://www.slideshare.net/RodolfoGarcia14/pitch-para-startups', 'pitch')
    compara = '{"Ocorrencias": 17}'
    json.dumps(compara)
    assert data == compara

def test_count4():
    data = api.count('http://www.wowgirl.com.br/guias/classes/bruxos/', 'bruxo')
    compara = '{"Ocorrencias": 45}'
    json.dumps(compara)
    assert data == compara

def test_count5():
    data = api.count('http://www.maua.br/conheca-maua', 'Ricardo')
    compara = '{"Ocorrencias": 2}'
    json.dumps(compara)
    assert data == compara

def test_count6():
    data = api.count('https://pythonhelp.wordpress.com/2014/08/05/web-scraping-com-scrapy-primeiros-passos/', 'Spider')
    compara = '{"Ocorrencias": 19}'
    json.dumps(compara)
    assert data == compara

def test_count7():
    data = api.count('https://docs.pytest.org/en/latest/assert.html', 'version')
    compara = '{"Ocorrencias": 7}'
    json.dumps(compara)
    assert data == compara

def test_count8():
    data = api.count('https://www.tecmundo.com.br/seguranca/119116-adeus-russos-governo-eua-remove-kaspersky-lista-parceiros.htm', 'russos')
    compara = '{"Ocorrencias": 1}'
    json.dumps(compara)
    assert data == compara

def test_count9():
    data = api.count('http://www.techtudo.com.br/noticias/2017/06/god-of-war-uncharted-o-que-esperar-da-conferencia-da-sony-na-e3-2017.ghtml', 'Last')
    compara = '{"Ocorrencias": 3}'
    json.dumps(compara)
    assert data == compara

def test_count10():
    data = api.count('https://olhardigital.com.br/pro/noticia/25-cursos-gratuitos-de-tecnologia-da-informacao/68684?utm_content=bufferee168&utm_medium=social&utm_source=plus.google.com&utm_campaign=buffer', 'SQL')
    compara = '{"Ocorrencias": 1}'
    json.dumps(compara)
    assert data == compara
