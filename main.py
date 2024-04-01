from flask import Flask, request
from chat_with_documents import ask_and_get_answer, load_document, chunk_data, create_embeddings

data = load_document('three_little_pigs.txt')
chunks = chunk_data(data)
vectorstore = create_embeddings(chunks)

app = Flask(__name__)

@app.get('/')
def home():
    return {'name':'Ottara'}

@app.post('/name')
def name():
    data = request.get_json()
    answer = ask_and_get_answer(vectorstore, data['q'])
    return answer

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)