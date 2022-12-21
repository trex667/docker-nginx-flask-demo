from flask import Flask, request
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    logging.basicConfig(level=logging.INFO)
    app.logger.info(request)
    return "hello world!"
    
if __name__ == "__main__":
    app.run()
