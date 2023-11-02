import dataclasses


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


@dataclasses.dataclass
class SevenSegmentDisplayConfig:
    digit_config: SevenSegmentDigitConfig = dataclasses.field(
        default_factory=SevenSegmentDigitConfig
    )
    number_config: SevenSegmentNumberConfig = dataclasses.field(
        default_factory=SevenSegmentNumberConfig
    )
