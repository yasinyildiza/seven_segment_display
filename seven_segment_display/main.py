import argparse

from seven_segment_display.display import SevenSegmentDisplay


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="Seven Segment Display",
    )
    parser.add_argument(
        "number",
        type=str,
        help="start number",
    )
    parser.add_argument(
        "-p",
        "--precision",
        type=int,
        help="decimal precision",
        default=2,
    )

    args = parser.parse_args()

    display = SevenSegmentDisplay(number=args.number, precision=args.precision)
    print(display)
