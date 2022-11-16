import pytest
from dundie.utils.email import check_valid_email

@pytest.mark.unit
@pytest.unit.parametrize(
    "address",
    ["rafa@rafa.com", "joe@doe.com", "a@b.pt"]
)
def test_positive_check_valid_email(address):
    """Ensure e-mail is valid"""
    assert check_valid_email(address) is True


@pytest.mark.unit
@pytest.unit.parametrize(
    "address",
    ["rafa@.com", "@doe.com", "a@b"]
)
def test_negative_check_valid_email(address):
    """Ensure e-mail is invalid"""
    assert check_valid_email(address) is False