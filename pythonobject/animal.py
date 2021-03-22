import yaml


# 创建一个动物类
class Animal:
    # 静态属性
    name = None
    color = None
    age = 0
    gender = "男"

    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    # 动态方法
    def call(self):
        print(f"{self.name} 会叫")

    def run(self):
        print(f"{self.name} 会跑")


# 创建子类【猫】
class Cat(Animal):

    # 添加一个新的属性，毛发=短毛
    hair = "短毛"

    # 复写父类的__init__方法，继承父类的属性
    def __init__(self, name, color, age, gender, hair):
        super().__init__(name, color, age, gender)
        self.hair = hair

    # 添加一个新的方法， 会捉老鼠
    def catch(self):
        print(f"{self.name} 会捉老鼠")

    # 复写父类的‘【会叫】的方法，改成【喵喵叫】
    def call(self):
        print("喵喵叫")


# 创建子类【狗】
class Dog(Animal):

    # 添加一个新的属性，毛发=长毛
    hair = "长毛"

    # 复写父类的__init__方法，继承父类的属性
    def __init__(self, name, color, age, gender, hair):
        super().__init__(name, color, age, gender)
        self.hair = hair

    # 添加一个新的方法， 会看家
    def home(self):
        print(f"{self.name} 会看家")

    # 复写父类的‘【会叫】的方法，改成【汪汪叫】
    def call(self):
        print("汪汪叫")


if __name__ == '__main__':
        cat = Cat("Kitty", "白色", "3", "女", "短毛")
        cat.catch()
        print(cat.name,
              cat.color,
              cat.age,
              cat.gender,
              cat.hair,
              "捉到老鼠了")

        dog = Dog("Tom", "棕色", "1", "男", "长毛")
        dog.home()
        print(dog.name,
              dog.color,
              dog.age,
              dog.gender,
              dog.hair,)

with open("./data/animal.yaml", encoding='utf-8') as f:
    print(yaml.safe_load(f))