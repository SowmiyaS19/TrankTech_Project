import pytest

from pages.verticals import vertical

@pytest.mark.smoke
def test_custom_app(page):
    obj_vertical=vertical(page)
    obj_vertical.customAppClick()