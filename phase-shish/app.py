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


# Create a store and get info
@app.get('/store')
def get_stores():
    return {"stores": stores}

# Create items for any shop 
@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name" : request_data["name"],"item" : []}
    stores.append(new_store)
    return new_store, 201

# Create special item
@app.post("/store/<string:name>/item")
def creatre_item():
    request_data = request.get_json()
    for store in stores :
        if store["name"] == name
            new_item = {"name" : request_data["name"], "price" : request_data["price"]}
            store["items"].append(new_item)
            return new_item,201
        return {"message" : "store is not found !"},404

# get a special store or item
@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name
            return store
        return {"message" : "Store is not found"},404@app.get("/store/<string:name>")
def get_item_in_store(name):
    for store in stores:
        if store["items": store["items"]] == name
            return store
        return {"message" : "Store is not found"},404