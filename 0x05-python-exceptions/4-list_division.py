#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            quotient = my_list_1[j] / my_list_2[j]
            new_list = quotient
        except ZeroDivisionError:
            print('division by 0')
        except ValueError:
            print('wrong type')
        except IndexError:
            print('out of range')
        finally:
            
            return(new_list)
