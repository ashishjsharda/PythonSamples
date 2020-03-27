class Parent:
    total=100
    def show(self):
        print("Total seen in parent is",Parent.total)

class Child(Parent):
    def show(self):
        print("In Child method")
        super(Child, self).show()

c=Child()
c.show()
