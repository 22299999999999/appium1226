import pytest

from po.page.app import App


@pytest.mark.parametrize("username,phone", [("name123", "13000000079"), ("name123", "13000000080")])
def test_add_member(username, phone):
    app = App()
    app.start()
    app.goto_main().goto_con().goto_invite_page().goto_add_member().add_member(username, phone)
