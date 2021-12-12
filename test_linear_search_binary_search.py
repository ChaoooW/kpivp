# -*- coding: utf-8 -*-

def test_linear_search_binary_search():
  import linear_search_binary_search
  assert linear_search_binary_search.binary_search([47, 39, 9, 22, 33, 19, 49, 2, 30, 3], 33) != -1
  assert linear_search_binary_search.linear_search([47, 39, 9, 22, 33, 19, 49, 2, 30, 3], 33) != -1