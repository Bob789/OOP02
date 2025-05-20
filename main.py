from customer import Customer



def main():
    c1 = Customer("Robert", "robert@gmail.com", 51)
    c2 = Customer("Bela", "bela@gmail.com", 32)
    customers = [c1,c2]
    print(customers)

    c1.set_id = 44
    print("New c1 id value: ", c1.id)

    c2.set_id = -1
    print("New c2 id value: ", c2.id)
    print(repr(c2))




if __name__ == "__main__":
    main()