import curses
import typer
from datetime import datetime
from currency_converter import CurrencyConverter

class CurrencyConverterWrapper:
    """
    A wrapper class for the CurrencyConverter library.
    """
    def __init__(self):
        """
        Initialize the CurrencyConverter object.
        """
        self.converter = CurrencyConverter()

    def convert(self, amount, from_currency, to_currency, conversion_date=None):
        """
        Convert the given amount from one currency to another.

        Parameters:
        amount (float): The amount to convert.
        from_currency (str): The currency to convert from.
        to_currency (str): The currency to convert to.
        conversion_date (str): The date of the conversion (optional).

        Returns:
        float: The converted amount.
        """
        if conversion_date:
            return self.converter.convert(amount, from_currency, to_currency, date=conversion_date)
        else:
            return self.converter.convert(amount, from_currency, to_currency)

    def get_currency_bounds(self, currency):
        """
        Get the bounds of the given currency.

        Parameters:
        currency (str): The currency to get the bounds for.

        Returns:
        tuple: The bounds of the currency.
        """
        return self.converter.bounds.get(currency, (None, None))

    def is_currency_supported(self, currency):
        """
        Check if the given currency is supported.

        Parameters:
        currency (str): The currency to check.

        Returns:
        bool: True if the currency is supported, False otherwise.
        """
        return currency in self.converter.currencies

app = typer.Typer()

@app.command()
def convert():
    """
    Prompt the user for an amount and two currencies, then convert the amount from the first currency to the second.
    """
    amount = float(typer.prompt("Enter the amount"))
    from_currency = typer.prompt("Enter the from currency")
    to_currency = typer.prompt("Enter the to currency")
    conversion_date = typer.prompt("Enter the conversion date in YYYY-MM-DD format (optional)", default="")
    
    wrapper = CurrencyConverterWrapper()
    if conversion_date:
        conversion_date = datetime.strptime(conversion_date, '%Y-%m-%d').date()
    result = wrapper.convert(amount, from_currency, to_currency, conversion_date)
    typer.echo(f"{amount} {from_currency} = {result} {to_currency}")

@app.command()
def is_supported(currency: str):
    """
    Check if the given currency is supported and print the result.

    Parameters:
    currency (str): The currency to check.
    """
    wrapper = CurrencyConverterWrapper()
    if wrapper.is_currency_supported(currency):
        typer.echo(f"{currency} is a supported currency")
    else:
        typer.echo(f"{currency} is not a supported currency")

def main(stdscr):
    """
    The main function of the application. It runs in a loop, prompting the user for a choice and executing the corresponding command.

    Parameters:
    stdscr (curses.window): The main window object provided by curses.
    """
    curses.echo()
    wrapper = CurrencyConverterWrapper()
    while True:
        stdscr.clear()
        stdscr.addstr("1. Convert currency\n")
        stdscr.addstr("2. Check if currency is supported\n")
        stdscr.addstr("3. Exit\n")
        stdscr.addstr("Enter your choice: ")
        stdscr.refresh()
        choice = stdscr.getstr().decode('utf-8')

        if choice == '1':
            stdscr.clear()  # Clear the screen
            stdscr.addstr("Enter the amount: ")
            amount = float(stdscr.getstr().decode('utf-8'))
            stdscr.addstr("Enter the from currency: ")
            from_currency = stdscr.getstr().decode('utf-8')
            stdscr.addstr("Enter the to currency: ")
            to_currency = stdscr.getstr().decode('utf-8')
            stdscr.addstr("Enter the conversion date in YYYY-MM-DD format (optional): ")
            conversion_date = stdscr.getstr().decode('utf-8')
            if conversion_date:
                conversion_date = datetime.strptime(conversion_date, '%Y-%m-%d').date()
            result = wrapper.convert(amount, from_currency, to_currency, conversion_date)
            stdscr.addstr(f"{amount} {from_currency} = {result} {to_currency}\n")
        elif choice == '2':
            stdscr.clear()  # Clear the screen
            stdscr.addstr("Enter the currency: ")
            currency = stdscr.getstr().decode('utf-8')
            if wrapper.is_currency_supported(currency):
                stdscr.addstr(f"{currency} is a supported currency\n")
            else:
                stdscr.addstr(f"{currency} is not a supported currency\n")
        elif choice == '3':
            break
        else:
            stdscr.clear()  # Clear the screen
            stdscr.addstr("Invalid choice. Please enter 1, 2, or 3.\n")
        stdscr.addstr("Press any key to continue...")
        stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)