
class Base2:
    def initial(self):
        print("base 2 initial")

    def response(self):
        # self.handle_log()
        print("base 2 response")

class Base:
    def initial(self):
        print("base 1 initial")
        super().initial()

    def response(self):
        self.handle_log()
        print("base 1 response")

    def handle_log(self):
        raise NotImplementedError # in yani man yek mixin hastam va niaz dram be impelement handle_log
        # ta betoonm to method reponse dorost ejra besham
    
    def test_child_method(self):
        self.my_child_method()

class Child(Base,Base2):
    def handle_log(self):
        print("this is handle log")
    def initial(self):
        print("child initial")
        return super().initial()
    def my_child_method(self):
        print("this is my child method")
    

c = Child()
# b = Base()
# b.response()
# c.response()
# help(c)

c.test_child_method()
