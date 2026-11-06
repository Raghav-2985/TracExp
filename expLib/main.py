import json 


class dtman():
    def __init__(self):
        self.mem = {id:{}}
        self.id = 0
    def add_entry(self , desc , amnt):
        desc = self.desc
        amnt = self.amnt
        template = {"description":desc , "amount":amnt}
        self.mem[id][self.id] = template
        self.id = self.id +1


