
class tr:
    def __init__(self, src: str, trans: str):
        if not isinstance(src, str) or len(src) == 0:
            raise TypeError('src argument is invalid')
        if not isinstance(trans, str) or len(trans) == 0:
            raise TypeError('translation argument is invalid')
        while len(trans) < len(src):
            trans += trans[-1]

        self.src = src
        self.trans = trans

    def xlate(self, instr: str):
        print(f"src={self.src}   trans={self.trans}")
        retstr = ''
        for ch in instr:
            index = self.src.find(ch)
            if index == -1:
                retstr += ch
            else:
                retstr += self.trans[index]

        return retstr

    def __call__(self, instr: str):
        return self.xlate(instr)
