import random

class Project():
    def __init__(self,data) -> None:
        self.data = data

    def GetRandomData(self):
        project_list = (list)(self.data.keys())
        proj = project_list[random.randrange(0,len(project_list))]
        sub_proj = self.GetRandomSub(proj)
        return " ".join([proj, sub_proj]) 
    
    def GetRandomSub(self,project:str):
        current_project = self.data[project]
        return current_project[random.randrange(0,len(current_project))]