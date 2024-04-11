from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/api/details', methods=['POST', 'GET'])
def index():
    print(f'\n request: {request}')
    return make_response({
          "client_status_code": 200,
          "message": "success"
    })



if __name__ == '__main__':
	app.run(debug=True, port=5000)
