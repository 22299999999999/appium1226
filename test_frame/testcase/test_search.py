from test_frame.app import App


class TestSearch():

    def test_search(self):
        app = App()
        app.start()
        result = app.goto_main().goto_hangqing().goto_search().search()
        assert result
