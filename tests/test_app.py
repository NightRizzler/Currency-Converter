def test_convert(converter):
    # Replace 'USD', 'EUR' and 100 with the actual currencies and amount you want to test
    result = converter.convert('USD', 'EUR', 100)
    # Check if the result is a float, which indicates a successful conversion
    assert isinstance(result, float)

def test_is_currency_supported(converter):
    assert converter.is_currency_supported('USD') == True
    assert converter.is_currency_supported('XYZ') == False