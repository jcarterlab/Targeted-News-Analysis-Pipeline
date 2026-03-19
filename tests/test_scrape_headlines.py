import pytest
from bs4 import BeautifulSoup
from news_monitoring_pipeline.scrape_headlines import extract_text


# ----------------------------------------------------------------------
# FIXTURES 
# ----------------------------------------------------------------------

@pytest.fixture
def make_headline_element():
    def _make(headline_html):
        soup = BeautifulSoup(headline_html, 'html.parser')
        return soup.find('a')
    return _make


# ----------------------------------------------------------------------
# EXTRACT_TEXT 
# ----------------------------------------------------------------------

class TestExtractText:
    def test_returns_none_for_none(self):
        assert extract_text(None) is None

    def test_returns_none_for_empty_text(self, make_headline_element):
        element = make_headline_element('<a></a>')
        assert extract_text(element) is None

    def test_strips_whitespace(self, make_headline_element):
        element = make_headline_element('<a>  Hello world  </a>')
        assert extract_text(element) == 'Hello world'

    def test_returns_text_from_nested_tags(self, make_headline_element):
        element = make_headline_element('<a><span>Hello</span> world</a>')
        assert extract_text(element) == 'Hello world'

    def test_normalizes_internal_whitespace(self, make_headline_element):
        element = make_headline_element('<a>Hello     world</a>')
        assert extract_text(element) == 'Hello world'

    def test_normalizes_newlines_and_tabs(self, make_headline_element):
        element = make_headline_element('<a>Hello\n\tworld</a>')
        assert extract_text(element) == 'Hello world'

    def test_returns_none_when_get_text_raises(self):
        class DummyElement:
            def get_text(self, *args, **kwargs):
                raise Exception('Boom')
            
        assert extract_text(DummyElement()) is None

