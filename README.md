# crawler_flask
Simples API para contagem no número de ocorrências de determinada palavra em um site qualquer.


Modo para utilização:
 - Após iniciar o arquivo "api.py", acessar o mesmo através do web browser pelo endereço "localhost:5000/search", preencher o formulário inserindo a URL no input URL e a palavra no input da Palavra, então clique em "Verificar"
 
 A resposta será um Objeto JSON com os seguintes dados:
   {
    "Ocorrencias": Número de vezes que "word" aparece em "url".
   }
