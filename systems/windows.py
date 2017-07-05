#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import re, os


def linux_os_exec():

    #a = os.system('notepad 8.txt')
    b = os.popen('notepad 8.txt')
    print b.read()



if __name__ == "__main__":

    linux_os_exec()
    None