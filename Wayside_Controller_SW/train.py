import dataclasses

@dataclasses.dataclass(frozen=False)
class Train:
    """deprecated"""
    id: int
    authority: int
    suggested_speed: int