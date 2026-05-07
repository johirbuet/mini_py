def test_smoke_import():
    import minipy
    assert hasattr(minipy, '__all__')
