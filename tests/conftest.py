import os
import tempfile

import pytest

from web import create_app, init_db


@pytest.fixture
def app_test():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path},
        db_path)

    with app.app_context():
        db = init_db(app)
        db.init_app(app)
        db.create_all()
        app.secret_key = 'secret_key'

    yield app

    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    return app_test.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

