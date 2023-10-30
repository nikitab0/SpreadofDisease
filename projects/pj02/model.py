"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from typing import List
from random import random
import constants
from math import sin, cos, pi, sqrt


__author__ = "730393935"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> float:
        """Returns distance of two Point objects."""
        dist = sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
        return dist


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Increases the simulation by a tick(1/30 sec)."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()

    def contract_disease(self) -> None:
        """Assign the infected constant defined above to the sickness attribute of Cell."""
        if self.sickness != constants.IMMUNE and self.sickness == constants.VULNERABLE:
            self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Returns true if cell's sickness attribute = vulnerable and false when it is not."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """Returns true if cell's sickness attribute = infected and false when it is not."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False
    
    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable():
            return "gray"
        elif self.is_infected():
            return "lime"
        elif self.is_immune():
            return "blue violet"
        else:
            return "black"

    def contact_with(self, other: Cell) -> None:
        """If infected cell comes in contact with vulnerable cell,  vulnerable becomes infected."""
        if self.is_infected() and other.is_vulnerable():
            other.contract_disease()

    def immunize(self) -> None:
        """Assigns immune to sickness attribute of a Cell."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Determines if a Cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False


class Model:
    """The state of the simulation."""

    population: List[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected: int, immune: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if infected >= cells or infected <= 0:
            raise ValueError("Number of infected cells not in bounds.")
        if immune >= cells or immune < 0:
            raise ValueError("Number of immune cells not in bounds.")
        for _ in range(0, cells):
            start_loc = self.random_location()
            start_dir = self.random_direction(speed)
            self.population.append(Cell(start_loc, start_dir))
        for i in range(0, infected):
            self.population[i].contract_disease()
        for i in range(0, immune):
            self.population[i].immunize()
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle = 2.0 * pi * random()
        dir_x = cos(random_angle) * speed
        dir_y = sin(random_angle) * speed
        return Point(dir_x, dir_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        total: int = 0
        for i in range(0, len(self.population)):
            if self.population[i].is_immune() or self.population[i].is_vulnerable():
                total += 1
            if total == len(self.population):
                return True
        return False

    def check_contacts(self) -> None:
        """Compare the distance between every cell."""
        for i in range(0, len(self.population)):
            for j in range(0, len(self.population)):
                if self.population[i].location.distance(self.population[j].location) < constants.CELL_RADIUS:
                    self.population[j].contact_with(self.population[i])
                else:
                    ...
