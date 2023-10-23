import dataclasses
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


@dataclasses.dataclass
class SevenSegmentNumberConfig:
    digit_config: SevenSegmentDigitConfig = dataclasses.field(default_factory=SevenSegmentDigitConfig)
    number_config: SevenSegmentNumberConfig = dataclasses.field(default_factory=SevenSegmentNumberConfig)


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
    def __init__(self, digit: SevenSegmentDigit, config: SevenSegmentDigitConfig | None = None):
        self.digit = digit
        self.config = config or SevenSegmentDigitConfig()

    def horizontal_segment(self, value: bool) -> str:
        return self.config.horizontal_fill if value else self.config.horizontal_empty

    def vertical_segment(self, value: bool) -> str:
        return self.config.vertical_fill if value else self.config.vertical_empty

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
    def number(cls, n: int, config: SevenSegmentDigitConfig | None = None) -> typing.Self:
        if not 0 <= n <= 9:
            raise ValueError(f"unsupported number: {n}")

        return cls(digit=SevenSegmentDigit.number(n=n), config=config)

    @classmethod
    def minus(cls, config: SevenSegmentDigitConfig | None = None)  -> typing.Self:
        return cls(digit=SevenSegmentDigit.minus(), config=config)


class SevenSegmentNumber:
    def __init__(self, n: int, config: SevenSegmentNumberConfig | None = None) -> None:
        self.n = n
        self.config = config or SevenSegmentNumberConfig()

        self.digits = []

        if self.n == 0:
            degree = 0
        else:
            degree = int(math.log10(abs(self.n)))

        x = abs(self.n)
        for i in range(degree + 1):
            e = 10 ** (degree - i)
            k = int(x / e)

            digit = SevenSegmentDigitDisplay.number(n=k, config=self.config.digit_config)
            self.digits.append(digit)

            x -= k * e

        if self.n < 0:
            self.digits.insert(0, SevenSegmentDigitDisplay.minus(config=self.config.digit_config))

    @property
    def lines(self) -> list[str]:
        lines = []
        for i in range(5):
            line = self.config.number_config.digit_space.join([digit.lines[i] for digit in self.digits])
            lines.append(line)

        return lines

    def __str__(self) -> str:
        return "\n".join(self.lines)


def main():
    for i in range(-10000, 10000):
        number = SevenSegmentNumber(i)

        print(number.n)
        print(number)


if __name__ == "__main__":
    main()
