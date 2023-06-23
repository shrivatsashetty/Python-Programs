class Client:
    name = "default"
    phone = "(123)456-7890"
    email = "foo@bar.com"
    purchases = 0

def main(): # def i another function outside the scope of class
    firstClient = Client()
    firstClient.name = "James "
    firstClient.email = "james@xyz.com"
    print(firstClient.name)
    print(firstClient.phone)
    print(firstClient.email)
    print(firstClient.purchases)

main()
