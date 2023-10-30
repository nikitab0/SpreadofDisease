"""This specially named module makes the package runnable."""

import constants
from model import Model
from ViewController import ViewController


def main() -> None:
    """Entrypoint of simulation."""
    model = Model(constants.CELL_COUNT, constants.CELL_SPEED, constants.CELLS_INFECTED, constants.CELLS_IMMUNE)
    vc = ViewController(model)
    vc.start_simulation()


if __name__ == "__main__":
    main()
