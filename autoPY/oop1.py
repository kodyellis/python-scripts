class Employee:
    name = "Ben"
    designation = "CEO"
    sales = 6
    def saleTargets(self):
        if self.sales >= 5:
            print("it good")
        else: 
            print ("not good")
        
emploe1 = Employee()
emploe1.name
emploe1.saleTargets()
