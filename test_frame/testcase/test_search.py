from test_frame.basepage import BasePage
from test_frame.page.main import MainPage


class TestSearch():

    def test_search(self):
        basepage = BasePage()
        app = MainPage(basepage)
        result = app.goto_hangqing().goto_search().search()
        assert result
