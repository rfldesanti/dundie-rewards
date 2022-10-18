import pytest

MARKER = """\
unit: Mark unit tests
integration: Mark integration tests
high: High priority
medium: Medium priority
low: Low priority
"""

def pytest_configure(config):
    map(lambda line: config.addinivalue_line('markers', line), MARKER.split("\n"))

@pytest.fixture(autouse=True)
def go_to_tmpdir(request): #dependency injection
    tmpdir = request.getfixturevalue("tmpdir")
    with tmpdir.as_cwd():
        yield