import pytest
from app import CurrencyConverterWrapper

@pytest.fixture
def converter():
    return CurrencyConverterWrapper()

def test_convert(converter):
    # Replace 'USD', 'EUR' and 100 with the actual currencies and amount you want to test
    result = converter.convert('USD', 'EUR', 100)
    # Replace expected_result with the expected result of the conversion
    expected_result = 85
    assert result == expected_result

def test_is_currency_supported(converter):
    assert converter.is_currency_supported('USD') == True
    assert converter.is_currency_supported('XYZ') == False