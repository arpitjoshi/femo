from flask import Flask, render_template
from posts.models import db
from posts.routes import blog_routes

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)
app.register_blueprint(blog_routes)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
