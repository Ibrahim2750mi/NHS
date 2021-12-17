import random
from typing import Any, List, Tuple

import arcade

from src.constants import SPRITE_SCALING
from src.misc.item import Item


class Mob(arcade.Sprite):
    def __init__(self: Any, health: int, drops: List[Tuple[int, int]]) -> None:
        self.health = health
        self.drops = drops

    def random_move(self: Any) -> None:
        self.change_x += random.choices([0, 3, -3], weights=[3, 1, 1])

    def kill(self: Any) -> List[Item]:
        return [Item(True, 64, actual_amount=amt, block_id=_id) for amt, _id in self.drops]


class Cow(Mob):
    def __init__(self: Any, x: int, y: int, health: int) -> None:

        super().__init__(
            health,
            [(random.randint(1, 4), 300), (random.randint(1, 3), 301)]
        )
        arcade.Sprite.__init__(
            self, "assets/mobs/cow.png", SPRITE_SCALING, center_x=x, center_y=y
        )


class Sheep(Mob):
    def __init__(self: Any, x: int, y: int, health: int) -> None:

        super().__init__(
            health, [(random.randint(1, 4), 302), (random.randint(1, 3), 303)]
        )
        arcade.Sprite.__init__(
            self, "assets/mobs/sheep.png", SPRITE_SCALING, center_x=x, center_y=y
        )


class Chicken(Mob):
    def __init__(self: Any, x: int, y: int, health: int) -> None:

        super().__init__(
            health, [(random.randint(1, 4), 303), (random.randint(1, 2), 304)]
        )
        arcade.Sprite.__init__(
            self, "assets/mobs/sheep.png", SPRITE_SCALING, center_x=x, center_y=y
        )


# FIXME Fill in correct item (drop) IDs
