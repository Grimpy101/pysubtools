import typing
from subtitle.content import Content
from subtitle.time import Time


class SubtitleUnit:
    start: Time
    end: Time
    content: Content
    
    def __init__(self, start: Time, end: Time, content: Content) -> None:
        self.start = start
        self.end = end
        self.content = content
    
    @property
    def duration(self) -> Time:
        return self.end - self.start
   
    def character_count(self, count_whitespace: bool = False) -> int:
        return self.content.count_characters(count_whitespace)
    
    def overlaps(self, other: 'SubtitleUnit') -> bool:
        return self.start <= other.end and other.start <= self.end
    
    def distance(self, other: 'SubtitleUnit') -> Time:
        zero_time = Time(0)
        dist1 = max(zero_time, self.start - other.end)
        dist2 = max(zero_time, other.start - self.end)
        return dist1 + dist2
    
    def __unicode__(self) -> str:
        return f"SubtitleUnit[{self.start}][{self.end}][{self.content}]"
    
    def __str__(self) -> str:
        return self.__unicode__()


class Subtitle:
    def __init__(self, units: typing.List[SubtitleUnit] = []) -> None:
        self.units = units
        
    def add_unit(self, unit: SubtitleUnit) -> None:
        self.units.append(unit)
        
    def insert_unit(self, index: int, unit: SubtitleUnit) -> None:
        self.units.insert(index, unit)
    
    def remove_unit(self, unit: SubtitleUnit) -> None:
        self.units.remove(unit)
    
    def remove_unit_at_index(self, index: int) -> None:
        self.units.pop(index)