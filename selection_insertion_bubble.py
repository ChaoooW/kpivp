# -*- coding: utf-8 -*-
"""selection_insertion_bubble_.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oXTwR5YDfl9T_fpNlhMne_tBtpgYFPOg
"""

import random

#selection_sort
#time complexity: O(n^2)
#Space complexity: O(1)

def selection_sort(arr, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if arr[i] < arr[min_idx]:
                min_idx = i
        (arr[step], arr[min_idx]) = (arr[min_idx], arr[step])
    return arr


def print_list(arr, size):
    print()
    for i in range(size):
        print ("% d"% arr[i], end =",")
    print()

if __name__ == "__main__":
  print("generating int list...")
  int_list = random.sample(range(1, 50), 10)
  print_list(int_list, len(int_list))
  print(f'selection_sort')
  selection_sort(int_list, len(int_list))
  print_list(int_list, len(int_list))


#insertion_sort
#time complexity: O(n^2)
#Space complexity: O(1)

def insertion_sort(arr):
  for step in range(1, len(arr)):
    key = arr[step]
    j = step - 1
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]
      j = j - 1
      arr[j + 1] = key
  return arr


if __name__ == "__main__":
  print("generating int list...")
  int_list = random.sample(range(1, 50), 10)
  print_list(int_list, len(int_list))
  print(f'insertion_sort')
  insertion_sort(int_list)
  print_list(int_list, len(int_list))


#bubble_sort
#time complexity: O(n^2)
#Space complexity: O(1)
def bubble_sort(arr):
  for i in range(len(arr)):
    for j in range(0, len(arr) - i - 1):
      if arr[j] > arr[j + 1]:
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp
  return arr

if __name__ == "__main__":
  print("generating int list...")
  int_list = random.sample(range(1, 50), 10)
  print_list(int_list, len(int_list))
  print(f'bubble_sort')
  bubble_sort(int_list)
  print_list(int_list, len(int_list))