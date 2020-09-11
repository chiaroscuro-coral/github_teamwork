from flask import Flask, request, jsonify,send_file

from stickerrec import stickersrecommendation

app = Flask(__name__)
@app.route('/')
def index_page():
    return send_file('4.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.json.get('search_query')
    print(data)
    paths = stickersrecommendation(data)
    return jsonify(paths)

@app.route('/emojis/<filename>')
def return_image(filename):
	return send_file('/Users/files/Desktop/emojis/' + filename, mimetype='image/jpg')

app.run()
