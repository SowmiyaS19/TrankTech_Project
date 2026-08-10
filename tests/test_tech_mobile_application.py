import pytest

from pages.technologies import technologies

@pytest.mark.smoke
def test_mobile_application(page):
    obj_tech=technologies(page)
    obj_tech.mobileAppClick()