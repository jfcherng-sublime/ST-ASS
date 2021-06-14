from typing import List, Sequence, Union
import sublime

ListRegion = List[int]
RegionLike = Union[sublime.Region, ListRegion]
RegionsLike = Sequence[RegionLike]
