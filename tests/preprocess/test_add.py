from src.preprocess.add import add

def test_add_int():
    assert add(1, 2) == 3

def test_add_float():
    assert add(0.5, 0.25) == 0.75

def test_add_negative():
    assert add(-3, 5) == 2

def test_add_str_concat():
    # Python の仕様どおり、文字列は連結される
    assert add("uv", "-fast") == "uv-fast"
