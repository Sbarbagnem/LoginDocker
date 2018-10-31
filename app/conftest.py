import os
import tempfile

import pytest
from model import db, User, app

def init_db():
    db.init_app(app)

    db.create_all()

@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        init_db()

    yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])
