from constants import *
from time import sleep
def start():
    lang = input(lang_quest)
    return lang
def talking(l):
    print(global_dict[l][0])
    sleep(2)
    answ = input(global_dict[l][1])
    return answ
def answer(a,l):
    if a.lower() in good_dict[l]:
        print(global_dict[l][2])
    elif a.lower() in bad_dict[l]:
        print(global_dict[l][3])
