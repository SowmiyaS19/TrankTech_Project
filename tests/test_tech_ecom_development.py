import pytest

from pages.technologies import technologies

@pytest.mark.smoke
def test_ecom_development(page):
    obj_tech=technologies(page)
    obj_tech.ecomDevClick()