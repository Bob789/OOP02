class Customer:
    def __init__(self, name: str, email: str, id: int):
        self.name = name
        self.email = email
        self.__id = id
        print('new instance created',__class__)

    def __str__(self):
        return(f"Customer {self.name} (id: {self.__id}) - Email {self.email}")

    def __repr__(self):
        return(f"Customer (Name = <{self.name}>, Email = <{self.email}>, id = <{self.__id}>)")

    @property
    def id(self):
        return self.__id

    @id.setter
    def set_id(self, id: int):
        if id > 0:
            self.__id = id

