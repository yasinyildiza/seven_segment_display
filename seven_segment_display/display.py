import decimal
import math

from seven_segment_display.config import SevenSegmentDisplayConfig
from seven_segment_display.digit_display import SevenSegmentDigitDisplay


class SevenSegmentDisplay:
    def __init__(
        self,
        number: decimal.Decimal | str | float | int,
        config: SevenSegmentDisplayConfig | None = None,
        precision: int = 2,
    ) -> None:
        self.number = decimal.Decimal(number)
        self.config = config or SevenSegmentDisplayConfig()
        self.precision = precision

        self.digits = self.build_digits()

    def build_digits(self) -> list[SevenSegmentDigitDisplay]:
        digits = []

        if self.number < decimal.Decimal(0):
            digit = SevenSegmentDigitDisplay.minus(config=self.config.digit_config)
            digits.append(digit)

        a = int(self.number * (10**self.precision))

        if self.number == decimal.Decimal(0):
            degree = 0
        else:
            degree = int(math.log10(abs(a)))

        x = abs(a)
        for i in range(degree + 1):
            e = 10 ** (degree - i)
            k = int(x / e)

            digit = SevenSegmentDigitDisplay.number(
                n=k, config=self.config.digit_config
            )
            digits.append(digit)

            x -= k * e

        return digits

    def group_digits(
        self,
        digits: list[SevenSegmentDigitDisplay],
        i: int,
    ) -> str:
        return self.config.number_config.digit_space.join(
            [digit.lines[i] for digit in digits]
        )

    def decimal_seperator(self, i: int) -> str:
        return (
            self.config.number_config.decimal_point
            if i == 4
            else self.config.number_config.decimal_space
        )

    def integer_part(self, i: int) -> str:
        end_index = -self.precision
        digits = self.digits[0:end_index]

        return self.group_digits(digits=digits, i=i)

    def decimal_part(self, i: int) -> str:
        start_index = -self.precision
        digits = self.digits[start_index:]

        return self.group_digits(digits=digits, i=i)

    def line(self, i: int) -> str:
        if self.precision == 0:
            return self.group_digits(digits=self.digits, i=i)

        return "".join(
            [
                self.integer_part(i=i),
                self.decimal_seperator(i=i),
                self.decimal_part(i=i),
            ]
        )

    @property
    def lines(self) -> list[str]:
        return [self.line(i=i) for i in range(5)]

    @property
    def text(self) -> str:
        return "\n".join(self.lines)

    @property
    def exponent(self) -> decimal.Decimal:
        return decimal.Decimal(f"0E-{self.precision}")

    @property
    def value(self) -> decimal.Decimal:
        return self.number.quantize(self.exponent)

    def __str__(self) -> str:
        return f"{self.value}\n{self.text}"
