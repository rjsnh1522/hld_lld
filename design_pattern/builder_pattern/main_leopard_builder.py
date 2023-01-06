# Design Leopard Class
class Leopard:
    def __init__(self, color, name, gender):
        self.color = color
        self.name = name
        self.gender = gender


l = Leopard("yellow", 'leopard_1', "Male")

# issue with above code is
# 1. we will have to remember the position of the arguments
# 2. code is not backward compatible as if add any new variable we will have to change at many places.



### How to resolve this issue.
# 1. We can make getter setter for each variables but we now color and gender would be same in this case throughout
# its life. So if we are giving getter setter method to client they can change color and gender of the Leopard


class Leopard:
    def __init__(self, obj):
        self.color = obj.get_color()
        self.gender = obj.get_gender()
        self.name = obj.get_name()


class XBuilder:
    def __init__(self):
        self.__name = None
        self.__color = None
        self.__gender = None

    def set_color(self, color):
        self.__color = color
        return self

    def set_name(self, name):
        self.__name = name
        return self

    def set_gender(self, gender):
        self.__gender = gender
        return self

    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color

    def get_gender(self):
        return self.__gender


x = XBuilder()
x.set_color('red')
x.set_gender('male')
x.set_name('kala')

leo = Leopard(x)

# if we combine everything in one line

x = XBuilder().set_name('name').set_gender('gender').set_color('red')
leo = Leopard(x)

# still we are allowing user to initialize Leopard class
# istead of that we can do like this




class XBuilder:
    def __init__(self):
        self.__name = None
        self.__color = None
        self.__gender = None

    def set_color(self, color):
        self.__color = color
        return self

    def set_name(self, name):
        self.__name = name
        return self

    def set_gender(self, gender):
        self.__gender = gender
        return self

    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color

    def get_gender(self):
        return self.__gender

    def leopar_func(self):
        return Leopard(self)


leo = XBuilder().set_name('name').set_gender('gender').set_color('red').leopar_func()

# in Above code we are forcing user to make instance of builder class which is not good.
# so what we will do is we would make one inner class of Builder inside the Leopard class


class Leopard:
    def __init__(self,obj):
        self.name = obj.get_name()
        self.colour = obj.get_colour()
        self.gender = obj.get_gender()

    class Builder:
        def __init__(self):
            self.__name = None
            self.__colour = None
            self.__gender = None
        # We are using setter and getters to access the variables

        def set_colour(self,colour):
            self.__colour = colour
            return self

        def get_colour(self):
            return self.__colour

        def set_name(self,name):
            self.__name = name
            return self

        def get_name(self):
            return self.__name

        def set_gender(self,gender):
            self.__gender = gender
            return self

        def get_gender(self):
            return self.__gender

        def build(self):
            l = Leopard(self)
            return l


l = Leopard.Builder().set_colour("yellow").set_name("leopard_1").set_gender("male").build()

print(l.name, l.colour, l.gender)

# Yayyy finally we created builder design pattern.
