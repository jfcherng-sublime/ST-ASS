from typing import Sequence, Tuple, Union
import sublime

TupleRegion = Tuple[int, int]
RegionLike = Union[sublime.Region, TupleRegion]
RegionsLike = Sequence[RegionLike]
