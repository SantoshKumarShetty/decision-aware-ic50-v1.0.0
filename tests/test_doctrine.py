
def test_doctrine_not_removed():
    with open("DOCTRINE.md") as f:
        text = f.read()
    assert "Correlation is not upgraded to causation" in text
