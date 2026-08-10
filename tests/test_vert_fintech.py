import pytest

from pages.verticals import vertical

@pytest.mark.smoke
def test_fintech(page):
    obj_vertical=vertical(page)
    obj_vertical.fintechClick()