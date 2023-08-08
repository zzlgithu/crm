# 定义Person类
class T:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def __str__(self):
        return f'name = {self.name},age = {self.age},gender = {self.gender}'
t = T('za',21,'man')
print(t)
