import pytest

from pages.aboutus import socialMedia

@pytest.mark.smoke
def test_aboutus(page):
    obj_aboutus=socialMedia(page)
    obj_aboutus.socialmediapageclick()

    