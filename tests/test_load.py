import uuid
import pytest
from dundie.core import load
from .constants import PEOPLE_FILE

@pytest.fixture(scope="function", autouse=True)
def create_new_file(tmpdir):
    file_ = tmpdir.join("new_file.txt")
    file_.write("Isso é sujeira")
    yield
    file_.remove()

@pytest.mark.unit
@pytest.mark.high
def test_load():
    """Test function load function."""

    with open(f"arquivo_indesejado-{uuid.uuid4()}.txt", "w") as file_:
        file_.write("dados úteis somente para o teste")
    
    assert len(load(PEOPLE_FILE)) == 2
    # com breakpoint() é possível entrar no modo debugger durante a geração do testw
    assert load(PEOPLE_FILE)[0][0] == 'J'

@pytest.mark.unit
@pytest.mark.high
def test_load2():
    """Test function load function."""

    with open(f"arquivo_indesejado-{uuid.uuid4()}.txt", "w") as file_:
        file_.write("dados úteis somente para o teste")
    
    assert len(load(PEOPLE_FILE)) == 2
    # com breakpoint() é possível entrar no modo debugger durante a geração do testw
    assert load(PEOPLE_FILE)[0][0] == 'J'