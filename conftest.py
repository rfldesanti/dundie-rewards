import pytest
from unittest.mock import patch


MARKERS = """\
unit: Mark unit tests
integration: Mark integration tests
high: High priority
medium: Medium priority
low: Low priority
"""


def pytest_configure(config):
    map(
        lambda line: config.addinivalue_line("markers", line),
        MARKERS.split("\n"),
    )


@pytest.fixture(autouse=True)
def go_to_tmpdir(request):  # injeção de dependências
    tmpdir = request.getfixturevalue("tmpdir")
    with tmpdir.as_cwd():
        yield  # protocolo de generators


@pytest.fixture(autouse=True, scope="function")
def setup_testing_database(request):
    """For each test, create a database file in tmpdir
    force database.py to use that filepath
    """
    tmpdir = request.getfixturevalue("tmpdir")
    test_db = str(tmpdir.join("database.test.json"))
    with patch("dundie.database.DATABASE_PATH", test_db):
        yield
