import mysql.connector


class customerEmptyNameAddressException(Exception):
    pass


class Customers:
    def __init__(self):
        self.__mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="passNew@@123",
            database="thirdDb"
        )
        self.__cr = self.__mydb.cursor();

    def newCustomer(self, name, address):
        if len(name) != 0 and len(address) != 0:
            self.__cr.execute("insert into customers (name, address) values (%s, %s)", [name, address])
            self.__mydb.commit()
        else:
            raise customerEmptyNameAddressException();

    def getAllCustomers(self):
        self.__cr.execute("select * from customers")
        myResult = self.__cr.fetchall()
        for x in myResult:
            print(x)

    def getCustomerByID(cid):
        self.__cr.execute("select count (*) from customers where id=%s", [cid])
        mr = self.__cr.fetchone()
        return bool(mr[0])

    def getCustomerInfoByID(self, cid):
        self.__cr.execute("Select * from customers where id=%s", [cid])
        mr = self.__cr.fetchone()
        return {"name": mr[1], "address": mr[2]}

    def deleteCustomerByID(self, cid):
        self.__cr.execute("delete from customers where id=%s", [cid])
        self.__mydb.commit()

    def updateCustomerNameById(self, cid, newName):
        self.__cr.execute("update customers set name=%s where id=%s", [newName, cid])
        self.__mydb.commit()

    def updateCustomerAddressById(self, cid, newAddress):
        self.__cr.execute("update customers set address=%s where id=%s", [newAddress, cid])
        self.__mydb.commit()


# 1 new customer, 2 get all customers, 3 ask for customer id, 4 delete, 5 update

mainChoice = int(input("Enter your choice [1,2,3,4]: "))
cstrObj = Customers()
if mainChoice == 1:

    nameInp = input("Enter your Name: ")
    addressInp = input("Enter your address: ")

    cstrObj.newCustomer(nameInp, addressInp)
    print("A new customer has been added")

elif mainChoice == 2:

    cstrObj.getAllCustomers()

elif mainChoice == 3:

    customerIDInput = int(input("Enter Customer ID: "))

    if cstrObj.getCustomerByID(customerIDInput):
        print(info)
    else:
        print("Customer not found")

elif mainChoice == 4:

    customerIdInput = int(input("Enter Customer ID: "))

    if cstrObj.getCustomerById(customerIdInput):

        cstrObj.deleteCustomerById(customerIdInput)
        print("Customer has been deleted")

    else:
        print("Customer has not been found")

elif mainChoice == 5:

    secondAction = input("Press N to update name, Press A to update address: ")

    customerIdInput = int(input("Enter Customer ID: "))

    if secondAction.upper() == 'N':

        newNameInput = input("Enter new name: ")
        cstrObj.updateCustomerNameById(customerIdInput, newNameInput)
        print("Name updated")

    elif secondAction.upper() == 'A':

        newAddressInput = input("Enter new address: ")
        cstrObj.updateCustomerAddressById(customerIdInput, newAddressInput)
        print("address updated")

    else:
        print("Invalid Action")
else:
    print("Yet to be implemented")
