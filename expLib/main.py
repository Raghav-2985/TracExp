import json 


class dtman():
    def __init__(self):
        self.mem = {"id":{}}
        self.id = 0
    def add_entry(self , desc , amnt):
        self.desc = desc
        self.amnt = amnt
        template = {"description":desc , "amount":amnt}
        self.mem["id"][self.id] = template
        self.id = self.id +1
    def show(self):
        list = json.dumps(self.mem , indent=4)
        print(list)

    def del_entry(self, Id):
        self.id = Id
        try:
            del self.mem["id"][Id]
        except KeyError:
            print("Id not found. Please enter a valid id or check the full expense list")

    

        