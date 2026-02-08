import pytest

@pytest.mark.dependency()
def test_pivotal_feature():
    """This is the core test that others depend on."""
    assert True

@pytest.mark.dependency(depends=["test_pivotal_feature"])
def test_dependent_feature():
    """This test will only run if test_pivotal_feature passes."""
    assert True