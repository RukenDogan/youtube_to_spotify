from flask_migrate import upgrade

def run_migrations(app):
    with app.app_context():
        upgrade()