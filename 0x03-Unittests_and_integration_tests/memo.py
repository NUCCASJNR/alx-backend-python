from utils import memoize
class TestClass:

    def a_method(self):
        return 42

    @memoize
    def a_property(self):
        return self.a_method()

obj = TestClass()
new_obj = obj.a_method()
print(new_obj)
print(obj.a_property)