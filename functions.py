def hows_the_parrot():
    print("He's pining for the fjords!")

hows_the_parrot()

def lumberjack(name):
    if name.lower() == 'kenneth':
        print("Kenneth's a lumber and he's OK!")
    else:
        print("{} sleeps all night and {} works all day!".format(name, name))

lumberjack("Corey")


def lumberjack(name, pronoun):
        print("{}'s a lumberjack and {} OK!".format(name, pronoun))

lumberjack("Kenneth", "he's")
lumberjack("Corey", "she's")
lumberjack("Chirada", "they're")


def product(num1, num2):
    return(num1*num2)

num1(20)
num2(10)

print(product)