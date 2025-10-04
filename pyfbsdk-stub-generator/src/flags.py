import enum

class GeneratorFlag(enum.Flag):
    NONE = 0
    CACHE = enum.auto()