from flask import Flask
from flask import Response
import Demo
import json
from Stock import Stock

app= Flask("_main_")

@app.route('/hello')
def index() :
    result= Demo.area(1, 2)
    print(result);
    return "Hello World";

@app.route('/getStock')
def getStock() :
        stockJson = stockApple()
        return Response(stockJson, content_type='application/json');


def stockApple():
    stock = Stock('Apple', 'APPL', '12.5')
    stockJson = json.dumps(stock.__dict__);
    print(' STOCK JSON ', stockJson)
    return stockJson


if __name__ == '__main__':
    app.run(debug=True)

