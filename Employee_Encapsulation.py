class Employee:
    __empid=0
    __empname= " "
    __empage=0
    __empdesignation=" "
    __empAddress= " "

    def setempid(self,id):
        self.__empid=id
    def getempid(self):
        return self.__empid

    def setempname(self,name):
        self.__empname=name
    def getempname(self):
        return self.__empname

    def setempage(self,age):
        self.__empage=age
    def getempage(self):
        return self.__empage
    def setempdesignation(self,designation):
         self.__empdesignation=designation
    def getempdesignation(self):
        return self.__empdesignation
    def setempAddress(self,address):
        self.__empAddress=address
    def getempAddress(self):
        return self.__empAddress
e=Employee()
e.setempid(432)
print(e.getempid())
e.setempname("Rohan")
print(e.getempname())
e.setempage(20)
print(e.getempage())
e.setempdesignation("Emp")
print(e.getempdesignation())
e.setempAddress("Cuttack")
print(e.getempAddress())