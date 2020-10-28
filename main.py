import view  # Do not delete!
from app import app
from app import db  # Do not delete!
from experiment.blueprint import experiment
from posts.blueprint import posts

app.register_blueprint(posts, url_prefix='/blog')
app.register_blueprint(experiment, url_prefix='/experiment')

if __name__ == '__main__':
    app.run()
