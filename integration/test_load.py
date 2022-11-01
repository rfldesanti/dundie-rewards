import pytest
<<<<<<< Updated upstream
from subprocess import check_output
=======
from click.testing import CliRunner
from dundie.cli import main, load
from .constants import PEOPLE_FILE

cmd = CliRunner()

>>>>>>> Stashed changes

@pytest.mark.integration
@pytest.mark.medium
def test_load():
    """Test command load"""
<<<<<<< Updated upstream
    out = check_output(
        ["dundie",
         "load",
          "tests/assets/people.csv"]
    ).decode("utf-8").split("\n")
    assert len(out) == 2
=======
    out = cmd.invoke(load, PEOPLE_FILE)
    assert "Dunder Mifflin Associates" in out.output


@pytest.mark.integration
@pytest.mark.medium
@pytest.mark.parametrize("wrong_command", ["loady", "carrega", "start"])
def test_load_negative_call_load_command_with_wrong_params(wrong_command):
    """Test command load"""
    out = cmd.invoke(main, wrong_command, PEOPLE_FILE)
    assert out.exit_code != 0
    assert f"No such command '{wrong_command}'." in out.output
>>>>>>> Stashed changes
