import pytest

from pages.contactus import contactus

@pytest.mark.smoke
def test_trading(page):
    obj_contact=contactus(page)
    obj_contact.contactusfill()