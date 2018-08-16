# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 22:09:22 2018

@author: Dean
"""
a = 2
print(a.__class__)
print(a.__class__.__class__)


class Foo:
    bar = True


class Foochild(Foo):
    pass


def echo_bar(self):
    print(self.bar)
    
Foochild = type("Foochild", (Foo,),{'echo_bar': echo_bar})

my_foo = Foochild()
my_foo.echo_bar()
