import dataclasses
import decimal
import math
import typing


@dataclasses.dataclass
class SevenSegmentDigitConfig:
    horizontal_empty: str = "   "
    horizontal_fill: str = "---"
    vertical_empty: str = " "
    vertical_fill: str = "|"
    vertical_space: str = " "


@dataclasses.dataclass
class SevenSegmentNumberConfig:
    digit_space: str = "   "
    decimal_point: str = " . "
    decimal_space: str = "   "
    decimal_precision: int = 2


@dataclasses.dataclass
class SevenSegmentDisplayConfig:
    digit_config: SevenSegmentDigitConfig = dataclasses.field(
        default_factory=SevenSegmentDigitConfig
    )
    number_config: SevenSegmentNumberConfig = dataclasses.field(
        default_factory=SevenSegmentNumberConfig
    )


@dataclasses.dataclass
class SevenSegmentDigit:
    a: bool = False
    b: bool = False
    c: bool = False
    d: bool = False
    e: bool = False
    f: bool = False
    g: bool = False

    @classmethod
    def zero(cls) -> typing.Self:
        return cls(
            a=True,
            b=True,
            c=True,
            d=True,
            e=True,
            f=True,
            g=False,
        )

    @classmethod
    def one(cls) -> typing.Self:
        return cls(
            a=False,
            b=True,
            c=True,
            d=False,
            e=False,
            f=False,
            g=False,
        )

    @classmethod
    def two(cls) -> typing.Self:
        return cls(
            a=True,
            b=True,
            c=False,
            d=True,
            e=True,
            f=False,
            g=True,
        )

    @classmethod
    def three(cls) -> typing.Self:
        return cls(
            a=True,
            b=True,
            c=True,
            d=True,
            e=False,
            f=False,
            g=True,
        )

    @classmethod
    def four(cls) -> typing.Self:
        return cls(
            a=False,
            b=True,
            c=True,
            d=False,
            e=False,
            f=True,
            g=True,
        )

    @classmethod
    def five(cls) -> typing.Self:
        return cls(
            a=True,
            b=False,
            c=True,
            d=True,
            e=False,
            f=True,
            g=True,
        )

    @classmethod
    def six(cls) -> typing.Self:
        return cls(
            a=True,
            b=False,
            c=True,
            d=True,
            e=True,
            f=True,
            g=True,
        )

    @classmethod
    def seven(cls) -> typing.Self:
        return cls(
            a=True,
            b=True,
            c=True,
            d=False,
            e=False,
            f=False,
            g=False,
        )

    @classmethod
    def eight(cls) -> typing.Self:
        return cls(
            a=True,
            b=True,
            c=True,
            d=True,
            e=True,
            f=True,
            g=True,
        )

    @classmethod
    def nine(cls) -> typing.Self:
        return cls(
            a=True,
            b=True,
            c=True,
            d=True,
            e=False,
            f=True,
            g=True,
        )

    @classmethod
    def minus(cls) -> typing.Self:
        return cls(
            a=False,
            b=False,
            c=False,
            d=False,
            e=False,
            f=False,
            g=True,
        )

    @classmethod
    def number(cls, n: int) -> typing.Self:
        digits = [
            cls.zero,
            cls.one,
            cls.two,
            cls.three,
            cls.four,
            cls.five,
            cls.six,
            cls.seven,
            cls.eight,
            cls.nine,
        ]

        return digits[n]()


class SevenSegmentDigitDisplay:
    def __init__(
        self,
        digit: SevenSegmentDigit,
        config: SevenSegmentDigitConfig | None = None,
    ):
        self.digit = digit
        self.config = config or SevenSegmentDigitConfig()

    def horizontal_segment(self, value: bool) -> str:
        return (
            self.config.horizontal_fill
            if value
            else self.config.horizontal_empty
        )

    def vertical_segment(self, value: bool) -> str:
        return (
            self.config.vertical_fill
            if value
            else self.config.vertical_empty
        )

    def vertical_line(self, left: bool, right: bool) -> str:
        return "".join(
            [
                self.vertical_segment(left),
                self.config.vertical_space,
                self.vertical_segment(right),
            ]
        )

    @property
    def lines(self) -> list[str]:
        return [
            self.horizontal_segment(self.digit.a),
            self.vertical_line(self.digit.f, self.digit.b),
            self.horizontal_segment(self.digit.g),
            self.vertical_line(self.digit.e, self.digit.c),
            self.horizontal_segment(self.digit.d),
        ]

    def __str__(self) -> str:
        return "\n".join(self.lines)

    @classmethod
    def number(
        cls, n: int, config: SevenSegmentDigitConfig | None = None
    ) -> typing.Self:
        if not 0 <= n <= 9:
            raise ValueError(f"unsupported number: {n}")

        return cls(digit=SevenSegmentDigit.number(n=n), config=config)

    @classmethod
    def minus(
        cls,
        config: SevenSegmentDigitConfig | None = None,
    ) -> typing.Self:
        return cls(digit=SevenSegmentDigit.minus(), config=config)


class SevenSegmentDisplay:
    def __init__(
        self,
        n: decimal.Decimal | str | float | int,
        config: SevenSegmentDisplayConfig | None = None,
    ) -> None:
        self.n = decimal.Decimal(n)
        self.config = config or SevenSegmentDisplayConfig()

        self.digits = []

        if self.n < decimal.Decimal(0):
            self.digits.append(
                SevenSegmentDigitDisplay.minus(config=self.config.digit_config)
            )

        a = int(self.n * (10**self.config.number_config.decimal_precision))

        if self.n == decimal.Decimal(0):
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
            self.digits.append(digit)

            x -= k * e

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
        end_index = -self.config.number_config.decimal_precision
        digits = self.digits[0:end_index]

        return self.group_digits(digits=digits, i=i)

    def decimal_part(self, i: int) -> str:
        start_index = -self.config.number_config.decimal_precision
        digits = self.digits[start_index:]

        return self.group_digits(digits=digits, i=i)

    def line(self, i: int) -> str:
        if self.config.number_config.decimal_precision == 0:
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

    def __str__(self) -> str:
        return self.text

    @property
    def precision(self) -> int:
        return self.config.number_config.decimal_precision

    @property
    def exponent(self) -> decimal.Decimal:
        return decimal.Decimal(f"0E-{self.precision}")

    @property
    def value(self) -> decimal.Decimal:
        return self.n.quantize(self.exponent)

    def display(self) -> None:
        print(self.value)
        print(self.text)


def main():
    for n in range(-10000, 10000):
        SevenSegmentDisplay(n=n).display()


if __name__ == "__main__":
    main()
