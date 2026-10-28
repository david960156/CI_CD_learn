# 這是我們要測試的加法函式（故意寫錯成 a - b）
def add(a, b):
    return a - b

# 這是自動化測試：檢查 add(2, 3) 是不是等於 5
def test_add():
    assert add(2, 3) == 5
