#!/usr/bin/python3
def common_elements(set_1, set_2):
   list_1 = list(set_1)
   list_2 = list(set_2)
   return (unique for unique in list_1 if unique in list_2)
