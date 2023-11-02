from seven_segment_display.config import SevenSegmentDigitConfig
from seven_segment_display.digit import SevenSegmentDigit


class SevenSegmentDigitDisplay:
    def __init__(
        self,
        digit: SevenSegmentDigit,
        config: SevenSegmentDigitConfig | None = None,
    ):
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
    def number(
        cls, n: int, config: SevenSegmentDigitConfig | None = None
    ) -> "SevenSegmentDigitDisplay":
        if not 0 <= n <= 9:
            raise ValueError(f"unsupported number: {n}")

        return cls(digit=SevenSegmentDigit.number(n=n), config=config)

    @classmethod
    def minus(
        cls,
        config: SevenSegmentDigitConfig | None = None,
    ) -> "SevenSegmentDigitDisplay":
        return cls(digit=SevenSegmentDigit.minus(), config=config)
