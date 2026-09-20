from flask import Flask

app = Flask(__name__)

stores = [
    {
        'name': 'pgshop',
        'items': [
            {
                'name': 'chair',
                'price': 200
            }
        ]
    }
]


@app.get('/store')
def get_stores():
    return {"stores": stores}

@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name" : request_data["name"],"item" : []}
    stores.append(new_store)
    return new_store, 201