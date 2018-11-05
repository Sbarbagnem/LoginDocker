import os
import tempfile

import pytest
from web import app


@pytest.fixture
def client():

    yield app.test_client()

