integer = r'([\+-]?\d+)'
decimal = r'([\+-]?((\d+\.)|(\d+\.\d+)|(\.\d+)))'
pattern = f'({integer}|{decimal})([eE]{integer})?'
p = compile(pattern)

class Solution:
    def isNumber(self, s: str) -> bool:
        return p.fullmatch(s)
