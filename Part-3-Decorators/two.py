def verify(func):

    def inner(name):
        if name=="Modi":
            print("Modi is Prime Minister")
        else:
            return func(name)
    return inner


def greet(name):
    print("Hi -", name,"  GM")

greet("Rahul")
greet("Sonia")
greet("Modi")
greet("Sikandar")