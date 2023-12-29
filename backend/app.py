from flask import Flask, request, jsonify
from flask_cors import CORS
import lang_chain

app = Flask(__name__)
CORS(app)

class Server:
    index = None


@app.route("/query", methods=['POST'])
def handle_request():
    content = request.json
    print(content)

    response = lang_chain.query(Server.index,
                                request_text=content.get('requestText'),
                                mode=content.get('mode'),
                                length=content.get('length'),
                                values=content.get('values'),
                                platform=content.get('platform'))

    return jsonify({"content": response})


# launch server
if __name__ == "__main__":
    Server.index = lang_chain.load_model()
    app.run()

