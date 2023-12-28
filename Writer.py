from JsonManager import JsonManager
import random

class Writer:
    jsonManager: JsonManager
    selected_project: str 
    def __init__(self):
        self.jsonManager = JsonManager()
        self.selected_project = "ADD"
        self.Write()
        self.Write()
        self.Write()

    #jsonManager data(딕셔너리) 의 모든 아이템 리스트에서 랜덤 뽑기
    def Write(self):
        result = ""
        for key in self.jsonManager.data.keys():
            #순차적으로 key를 받는다
            current_item = self.jsonManager.data[key]
             #해당 key의 하위 아이템을 다 돌고 나온다
            result += self.GetRandomValue(current_item, "")
        result = self.LookOverResult(result)
        print(result)

    #선택 가능한 key일 경우 검사
    def CheckKey(self, key, target, result: str):
        if(key == self.jsonManager.PROJECT):
            return self.SelectProject(target, result)
        return ""
    
    def SelectProject(self, target, result: str):
        result += self.selected_project
        return self.GetRandomValue(target[self.selected_project], result)

    #dict,list 뒤섞인 값에서 모두 랜덤 추출하기(재귀 사용)
    def GetRandomValue(self, target, result: str):
        if type(target) is dict:#딕셔너리에서 key값을 뽑았으면 그 value도 랜덤추출검사
            temp = self.GetRandomKeyFromDict(target) 
            result += temp +" "
            return self.GetRandomValue(target[temp],result)
        elif type(target) is list: #리스트에서 값 뽑았으면 값만 리턴
            result += self.GetRandomFromList(target) +" "
        return result

    def GetRandomKeyFromDict(self, target:dict):
        return self.GetRandomFromList(list(target.keys()))

    #리스트에서 랜덤한 값을 리턴
    def GetRandomFromList(self, target:list):
        if len(target)>0:
            return target[random.randrange(0,len(target))]
        return ""
    
    #문장 검수
    def LookOverResult(self, result: str):
        result = result.rstrip()
        result += "."
        return result.replace("  ", " ")
