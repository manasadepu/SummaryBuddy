from flask import Flask, request, jsonify
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer


app = Flask(__name__)

@app.errorhandler(500)
def handle_500(error):
    app.logger.error(f"Internal error: {error}")
    return jsonify({"error": "Internal Server Error"}), 500

@app.route("/testing/<name>")
def get_name(name):

    msg = {
        "Welcome": f"Welcome to the summarize extension,{name}!"
    }

    return jsonify(msg), 200

@app.route("/summarize", methods=['POST'])
def summarize():
    text = request.data.decode('utf-8')

    if not text:
        error_msg = {
            "ERROR": "No text found"
       }
        
        return jsonify(error_msg)
    
    else:
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = TextRankSummarizer()
        SUMMARYLENGTH = 5

        summary = summarizer(parser.document, SUMMARYLENGTH)

        large_sentence = ""
        for sentence in summary:
            large_sentence += " " + str(sentence)

        text_response = {
            "text": large_sentence,
            "success": True,
            "accessed": "Yes, access successful"
        }

        return jsonify(text_response), 200

@app.route("/getsummary/<text>", methods=['GET'])
def get_summary(text):

    if not text:
        error_msg = {
            "ERROR": "No text found"
       }
        
        return jsonify(error_msg)
    
    else:
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = TextRankSummarizer()
        SUMMARYLENGTH = 5

        summary = summarizer(parser.document, SUMMARYLENGTH)

        large_sentence = ""
        for sentence in summary:
            large_sentence += " " + str(sentence)

        text_response = {
            "text": large_sentence,
            "success": True,
            "accessed": "Yes, access successful"
        }

        return jsonify(text_response), 200

@app.route("/")
def index():
    return "<h1>Welcome to summary buddy!</h1>"


if __name__ == '__main__':
    app.run(threaded=True, debug=True, port=5000)