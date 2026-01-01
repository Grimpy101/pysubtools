import typing


class Style:
    def __init__(self, style_type: str, start: int, end: int, value: typing.Any) -> None:
        self.style_type = style_type
        self.start = start
        self.end = end
        self.value = value
    
    def in_range(self, start: int, end: int) -> bool:
        return self.start <= end and start <= self.end
    
    def change_range(self, start: int, end: int) -> None:
        self.start = start
        self.end = end
    
    def __unicode__(self) -> str:
        return f"Style[{self.style_type}][{self.start}-{self.end}]"
    
    def __str__(self) -> str:
        return self.__unicode__()


class Content:
    def __init__(self, raw_text: str, styles: typing.List[Style]) -> None:
        self.raw_text = raw_text
        self.styles = styles
    
    def count_lines(self) -> int:
        return len(self.raw_text.splitlines())
    
    def count_characters(self, count_whitespace: bool = False) -> int:
        if not count_whitespace:
            return len("".join(self.raw_text.split()))
        return len(self.raw_text)
    
    def add_style(self, style: Style) -> None:
        self.styles.append(style)
        
    def remove_style(self, style: Style) -> None:
        self.styles.remove(style)
        
    def remove_style_type(self, style_type: str) -> None:
        self.styles = [stl for stl in self.styles if stl.style_type != style_type]
    
    def remove_style_in_range(self, start: int, end: int) -> None:
        self.styles = [stl for stl in self.styles if not stl.in_range(start, end)]
    
    def __unicode__(self) -> str:
        return self.raw_text.replace('\n', '|')
    
    def __str__(self) -> str:
        return self.__unicode__()