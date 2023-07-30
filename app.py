from flask import Flask, request, jsonify
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

app = Flask(__name__)

@app.route("/get-summary/<text>", methods=['GET'])
def get_summary(text):

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


