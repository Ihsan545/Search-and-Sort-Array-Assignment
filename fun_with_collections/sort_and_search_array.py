import array as arr
"""
Program: sort_and_search_array.py
Author: Ihsanullah Anwary
Last date modified: 10/07/2020
This program is an example sorting and searching array.
"""
n_arr = arr.array('d', [5,6,8,10,4,3,10,2,1])  # defining array.


def sort_array(sort_):
    """ sorting array"""
    for i in n_arr:

         array_to_list = sort_.tolist()
         sort_list = array_to_list.sort()
         sort_list  = arr.array('d', array_to_list)
         return sort_list


def search_array(key, value):
    """ searching for index in array"""
    try:
        key.index(value)
    except ValueError:
        return key


if __name__ == '__main__':
    sort_array(n_arr)
    print(search_array(value=-1, key=n_arr))
    """ printing the array list, it can not find -1 in the list"""
