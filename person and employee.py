class person( object ):
    def __init__(self,name,id_num):
        self.name = name
        self.id_num = id_num
    def display(self):
        print(self.id_num)
        print(self.name)
class employee(person):
    def __init__(self,name,id_num,salary,post):
        self.salary = salary
        self.post = post
        person.__init__(self,name,id_num)
a = employee("random guy",5775757,100000000,"BOSS")
a.display()