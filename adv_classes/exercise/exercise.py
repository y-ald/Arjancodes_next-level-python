from dataclasses import dataclass


@dataclass
class Circle:
    _radius: float

    # TODO: Add the properties


def main() -> None:
    circle = Circle(5.0)

    # Test the properties
    circle.radius = 10
    print("Radius:", circle.radius)
    print("Diameter:", circle.diameter)
    print("Area:", circle.area)
    print("Circumference:", circle.circumference)


if __name__ == "__main__":
    main()
