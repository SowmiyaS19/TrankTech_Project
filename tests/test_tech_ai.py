import pytest

from pages.technologies import technologies

@pytest.mark.smoke
def test_ai(page):
    obj_tech=technologies(page)
    obj_tech.aiClick()