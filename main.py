import requests
from flask import Flask, render_template, request
from contact import send_form

BLOG_URL = "https://api.npoint.io/37c6259edce6a9b716e9"

app = Flask(__name__)

@app.route('/')
def index():
    data = make_request()
    return render_template("index.html", posts=data)


@app.route("/post/<int:post_id>")
def post(post_id):
    data = make_request()
    blog_post = [i for i in data if i["id"] == post_id][0]
    return render_template("post.html", blog_post=blog_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/form_entry", methods=["POST"])
def form_entry():
    form_data = request.form.to_dict()
    send_form(form_data)
    return render_template("form_entry.html")


def make_request():
    response = requests.get(BLOG_URL)
    return response.json()


if __name__ == "__main__":
    app.run(debug=True)
