import random

class Act():
    def __init__(self,prefix,data,suffix) -> None:
        self.prefix = prefix
        self.data = data
        self.suffix = suffix
        self.current_belong = ""

    def GetRandomPrefix(self): #선택 안함 포함 랜덤 추출
        if self.prefix is None: return ""
        result = random.randrange(0,len(self.prefix)+1)
        if result >= len(self.prefix): return ""
        return self.prefix[result]

    def GetRandomData(self):
        all_list = [] #중심 그룹에서 모든 아이템을 가져와 랜덤으로 고른다
        for key in self.data.keys():
            for item in self.data[key]:
                all_list.append(item)
        result = all_list[random.randrange(0,len(all_list))]
        #선택된 아이템이 어느 카테고리에 있는지 확인한다
        self.current_belong = ""
        for key in self.data.keys():
            if item in self.data[key]: 
                self.current_belong = key
                break
        #선택된 카테고리에 맞는 suffix를 랜덤 추출 한다
        prefix = self.GetRandomPrefix()
        suffix = self.GetRandomSuffix()
        return " ".join([suffix,result,prefix])
            
    def GetRandomSuffix(self):
        if self.suffix is None: return ""
        selected_suffix = self.suffix[self.current_belong]
        result = self.selected_suffix[random.randrange(0,len(selected_suffix))]
        return selected_suffix[result]