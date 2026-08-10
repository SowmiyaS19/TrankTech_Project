import pytest

from pages.blog import blogmenus

@pytest.mark.smoke
def test_blogmenu(page):
    obj_blog=blogmenus(page)
    obj_blog.blogMenuClick()