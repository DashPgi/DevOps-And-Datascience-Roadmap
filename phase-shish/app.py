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