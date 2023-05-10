from flask import Flask

app = Flask(__name__) # __name__ is a special variable that is set to the name of the module in which it is used

print(__name__) # prints __main__ when run directly, but prints the name of the module when imported

@app.route('/', methods=['GET']) # the "@" symbol designates a "decorator" which attaches the following function to the '/' route('/', aca puedo pasar metodos como GET, POST, etc, si no se especifica, por defecto es GET)

def index():
    #patromnes de diseño modelo vista controlador
    # django usa el patron mvt (modelo vista template)
    return "Hello World!"

@app.route('/api', methods=['GET'])
def get():
    return {
        'message': 'Hello World!'
    }

@app.route('/api/<id>', methods=['POST'])
def post(id):
    return {
        'message': f'Hello World! NRO: {id}'
    }
# to make a post request, we need to install a package called postman or insomnia , so we can make a post request to our api and see the response

if __name__ == "__main__": # ensure this file is being run directly and not from a different module
    app.run(debug=True) # run the app in debug mode.
