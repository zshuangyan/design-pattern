# -*- coding: UTF-8 -*-
class Duck:
    def quack(self):
        print "這鴨子在呱呱叫"

    def feathers(self):
        print "這鴨子擁有白色與灰色羽毛"


class Person:
    def quack(self):
        print "這人正在模仿鴨子"

    def feathers(self):
        print "這人在地上拿起1根羽毛然後給其他人看"


def in_the_forest(duck):
    duck.quack()
    duck.feathers()


def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)


game()
