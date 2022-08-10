class SimpleCalc:

    def add(self, value1, value2):
        return value1 + value2

    def subtract(self,value1,value2):
         return value1 - value2

    def multiply(self,value1,value2):
         return value1*value2

    def divide(self,value1,value2):
         return value1/value2

    def conversion_cm_to_mtr(self,value1):
        return value1/100

    def percentage(self,value1,value2):
        return (value1/value2 *100)

    def DOB(self,value1,value2):
        return (f"Your DOB is {value1} / {value2}")


obj = SimpleCalc()
print(obj.DOB(1990,2))
