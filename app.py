from flask import Flask, render_template
from posts.routes import blog_routes
from connectors.mysql_extension import db

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)
app.register_blueprint(blog_routes)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
