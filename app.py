from flask import Flask, request, render_template
from pinecone_utils import query_pinecone

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        query = request.form["query"]
        subject = request.form.get("subject")
        topic = request.form.get("topic")
        answer = query_pinecone(query, subject, topic)
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
