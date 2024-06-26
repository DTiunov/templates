import io
import requests

from flask import Flask
from flask import request
from flask import Response
from flask import send_file

app = Flask(__name__)

@app.route('/<path:path>', methods=['GET'])
def screenshots(path):
    try:
        response = requests.get('https://<URL корзины DigitalOcean>/' + path)
    except:
        print('\n#######################')
        print('CLIENT REQUEST HEADERS:')
        print(request.headers)
        return Response(status=520)
    if response.status_code >= 500:
        print('\n#######################')
        print('CLIENT REQUEST HEADERS:')
        print(request.headers)
        print('DIGITAL OCEAN RESPONSE HEADERS:')
        print(response.headers)
        print((response.status_code))
        return Response(status=520)
    return send_file(io.BytesIO(response.content), mimetype=response.headers['content-type'])

if __name__ == '__main__':
    app.run(host="0.0.0.0")
