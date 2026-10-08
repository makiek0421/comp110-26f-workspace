"""Making art... a heart with an arrow thru it"""

from math import atan2, degrees, sqrt

from spacepaint import Ship, start_spacepaint

__author__: str = "730758115"


def main(aura: Ship) -> None:
    """Arrange the components of my scene"""
    aura.speed(multiplier=4.0)
    draw_love_art(ship=aura, x=0.0, y=0.0)
    counter: int = 0
    while counter < 3:
        draw_small_heart(ship=aura, x=-4.5 + counter * 0.5, y=-1.5 + counter * 1.5)
        counter = counter + 1
    return None


def angle_between(ship: Ship, x: float, y: float) -> float:
    """Compute the turn from the ship's heading toward an X/Y point."""
    change_y: float = y - ship.y
    change_x: float = x - ship.x
    if change_x == 0.0 and change_y == 0.0:
        return 0.0
    angle: float = atan2(change_y, change_x)
    angle_degrees: float = degrees(angle)
    turn: float = angle_degrees - ship.heading_x_y
    if turn > 180.0:
        turn = turn - 360.0
    else:
        if turn < -180.0:
            turn = turn + 360.0
    return turn


def distance_between(ship: Ship, x: float, y: float) -> float:
    """Compute the distance from the ship to an X/Y point."""
    change_y: float = y - ship.y
    change_x: float = x - ship.x
    distance: float = sqrt(change_y**2 + change_x**2)
    return distance


def move_to(ship: Ship, x: float, y: float) -> None:
    """Move the ship from its current position to an X/Y point."""

    ship.turn(degrees=angle_between(ship=ship, x=x, y=y))

    ship.forward(units=distance_between(ship=ship, x=x, y=y))


def square_at(
    ship: Ship,
    center_x: float,
    center_y: float,
    length: float,
) -> None:
    """Paint a square centered at an X/Y point."""
    half: float = length / 2.0
    ship.beam(on=False)
    move_to(ship=ship, x=center_x + half, y=center_y + half)
    ship.beam(on=True)
    move_to(ship=ship, x=center_x - half, y=center_y + half)
    move_to(ship=ship, x=center_x - half, y=center_y - half)
    move_to(ship=ship, x=center_x + half, y=center_y - half)
    move_to(ship=ship, x=center_x + half, y=center_y + half)

    ship.beam(on=False)


def draw_heart(ship: Ship, x: float, y: float, size: float) -> None:
    """Draw a heart centered at (x, y) using the given size."""
    ship.beam(on=False)
    ship.fill(on=False)
    ship.beam_color(value="red")
    move_to(ship=ship, x=x, y=y + size * 0.5)
    ship.fill(on=True, opacity=0.8)
    ship.beam(on=True)
    move_to(ship=ship, x=x - size * 0.25, y=y + size * 0.75)
    move_to(ship=ship, x=x - size * 0.45, y=y + size * 0.85)
    move_to(ship=ship, x=x - size * 0.70, y=y + size * 0.70)
    move_to(ship=ship, x=x - size * 0.75, y=y + size * 0.35)
    move_to(ship=ship, x=x - size * 0.50, y=y - size * 0.10)
    move_to(ship=ship, x=x, y=y - size * 0.85)
    move_to(ship=ship, x=x + size * 0.50, y=y - size * 0.10)
    move_to(ship=ship, x=x + size * 0.75, y=y + size * 0.35)
    move_to(ship=ship, x=x + size * 0.70, y=y + size * 0.70)
    move_to(ship=ship, x=x + size * 0.45, y=y + size * 0.85)
    move_to(ship=ship, x=x + size * 0.25, y=y + size * 0.75)
    move_to(ship=ship, x=x, y=y + size * 0.5)
    ship.fill(on=False)
    ship.beam(on=False)
    return None


def draw_arrow(ship: Ship, x: float, y: float) -> None:
    """Draw an arrow thru the heart near (x, y)."""
    ship.beam(on=False)
    ship.fill(on=False)
    ship.beam_color(value="white")
    move_to(ship=ship, x=x - 2.8, y=y - 1.7)
    ship.beam(on=True)
    move_to(ship=ship, x=x + 2.8, y=y + 1.7)
    move_to(ship=ship, x=x + 2.0, y=y + 1.8)
    move_to(ship=ship, x=x + 2.8, y=y + 1.7)
    move_to(ship=ship, x=x + 2.4, y=y + 0.95)
    ship.beam(on=False)
    return None


def draw_love_art(ship: Ship, x: float, y: float) -> None:
    """Draw a heart with an arrow through it."""
    draw_heart(ship=ship, x=x, y=y, size=3.0)
    draw_arrow(ship=ship, x=x, y=y)
    return None


def draw_small_heart(ship: Ship, x: float, y: float) -> None:
    """Draw a smaller heart at the given position."""
    draw_heart(ship=ship, x=x, y=y, size=0.5)
    return None


if __name__ == "__main__":
    start_spacepaint()
