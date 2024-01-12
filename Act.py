import random

class Act():
    def __init__(self,prefix,data,suffix) -> None:
        self.prefix = prefix
        self.data = data
        self.suffix = suffix
        self.current_belong = ""

    def GetRandomData(self, belong = ""):
        belong_list = self.data[belong]
        result = belong_list[random.randrange(0,len(belong_list))]
        prefix = self.GetRandomPrefix()
        suffix = self.GetRandomSuffix()
        return " ".join([prefix,result,suffix])
    
    def GetRandomPrefix(self): #선택 안함 포함 랜덤 추출
        if self.prefix is None: return ""
        result = random.randrange(0,len(self.prefix)+1)
        if result >= len(self.prefix): return ""
        return self.prefix[result]
            
    def GetRandomSuffix(self):
        if self.suffix is None: return ""
        result = self.suffix[random.randrange(0,len(self.suffix))]
        return result