rates = {
    "KGS": 1,
    "USD": 89,
    "EUR": 96,
    "RUB": 1.2
}


class Money:
    def __init__(self, amount: float, currency: str):
        self.amount = amount
        self.currency = currency.upper()

    def convert_to_kgs(self) -> float:
        if self.currency not in rates:
            raise ValueError(f"Валюта {self.currency} не поддерживается.")
        return self.amount * rates[self.currency]

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented

        if self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)

        total_kgs = self.convert_to_kgs() + other.convert_to_kgs()
        return Money(total_kgs, "KGS")

    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented

        if self.currency == other.currency:
            return Money(self.amount - other.amount, self.currency)

        total_kgs = self.convert_to_kgs() - other.convert_to_kgs()
        return Money(total_kgs, "KGS")

    def __mul__(self, number: float):
        if not isinstance(number, (int, float)):
            return NotImplemented
        return Money(self.amount * number, self.currency)

    def __truediv__(self, number: float):
        if not isinstance(number, (int, float)):
            return NotImplemented
        if number == 0:
            raise ZeroDivisionError("Деление на ноль невозможно.")
        return Money(self.amount / number, self.currency)

    def __str__(self) -> str:
        display_amount = int(self.amount) if self.amount == int(self.amount) else self.amount
        return f"{display_amount} {self.currency}"

if __name__ == "__main__":
    money1 = Money(100, "USD")
    money2 = Money(5000, "KGS")

    result_add = money1 + money2
    print(f"Сложение: {result_add}")

    result_sub = money1 - money2
    print(f"Вычитание: {result_sub}")  # Вывод: 3900 KGS


    result_mul = money1 * 3
    print(f"Умножение: {result_mul}")  # Вывод: 300 USD


    result_div = money2 / 2
    print(f"Деление: {result_div}")  # Вывод: 2500 KGS