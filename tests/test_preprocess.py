from emailclf.preprocess import clean_text
def test_clean_text_basic():
    assert clean_text("Hello!!! Buy NOW.") == "hello buy now"
