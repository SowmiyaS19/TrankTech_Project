import pytest

from pages.verticals import vertical

@pytest.mark.smoke
def test_retail_ecommerce(page):
    obj_vertical=vertical(page)
    obj_vertical.retailEcomClick()
    