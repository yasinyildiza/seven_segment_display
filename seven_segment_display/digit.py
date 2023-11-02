import dataclasses


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
    def zero(cls) -> "SevenSegmentDigit":
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
    def one(cls) -> "SevenSegmentDigit":
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
    def two(cls) -> "SevenSegmentDigit":
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
    def three(cls) -> "SevenSegmentDigit":
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
    def four(cls) -> "SevenSegmentDigit":
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
    def five(cls) -> "SevenSegmentDigit":
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
    def six(cls) -> "SevenSegmentDigit":
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
    def seven(cls) -> "SevenSegmentDigit":
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
    def eight(cls) -> "SevenSegmentDigit":
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
    def nine(cls) -> "SevenSegmentDigit":
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
    def minus(cls) -> "SevenSegmentDigit":
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
    def number(cls, n: int) -> "SevenSegmentDigit":
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
