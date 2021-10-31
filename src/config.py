from pathlib import Path

ASSET_DIR = (Path(__file__).parent.parent / "assets").resolve()
DATA_DIR = (Path(__file__).parent.parent / "data").resolve()

MAX_SLOTS = 10

SPRITE_SCALING = 1.0
INVENTORY_SCALING = (3/11) * MAX_SLOTS
PLAYER_SCALING = 1.0

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Box Adventures"
SPRITE_PIXEL_SIZE = 20
ICON_SIZE = 16
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * SPRITE_SCALING)

VIEWPORT_MARGIN = SPRITE_PIXEL_SIZE * SPRITE_SCALING
RIGHT_MARGIN = 4 * SPRITE_PIXEL_SIZE * SPRITE_SCALING

MOVEMENT_SPEED = 5 * SPRITE_SCALING
JUMP_SPEED = 24 * SPRITE_SCALING
GRAVITY = 1 * SPRITE_SCALING
PLAYER_BLOCK_REACH = 100 * PLAYER_SCALING  # 100 pixel reach to block

MAX_STACK = 99

MUSIC = False

CHUNK_WIDTH = 16
CHUNK_HEIGHT = 320

VISIBLE_RANGE_MAX = int((2.5 * CHUNK_WIDTH) / SPRITE_SCALING)
VISIBLE_RANGE_MIN = int((-2.5 * CHUNK_WIDTH) / SPRITE_SCALING)

CHUNK_WIDTH_PIXELS = SPRITE_PIXEL_SIZE * CHUNK_WIDTH
CHUNK_HEIGHT_PIXELS = SPRITE_PIXEL_SIZE * CHUNK_HEIGHT
