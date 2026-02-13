class Robot:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.battery = 100
        self.durability = 100
        self.productivity = 0




    def charge(self, amount):
        if self.battery < 100:
            self.battery = self.battery + int(amount)
        else:
            return f"{self.name} charged by {amount}."
    
    def work(self, amount):
        if self.battery < (int(amount) * 10):
            print("Can not work at all")
        else:
            self.battery = self.battery - (int(amount) * 10)
            self.durability = self.durability - (int(amount) * 5)
            self.productivity = self.productivity + (int(amount) * 8)
            if self.durability < 50:
                print("Warning Durability is below 50, Try Repairing")
            return f"{self.name} worked for {amount} hours."

    def repair(self):
        self.durability += 20
        self.productivity -=10
        return f"{self.name} has been repaired."


    def status(self):
        return f"{self.name}| Color: {self.color}| Battery: {self.battery}| Durability: {self.durability} | Productivity: {self.productivity}"


    #def recolor(self, amount):
        #pass



    def shutdown(self, amount):
        pass
        # initialize properties code here
        pass