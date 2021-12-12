def test_selection_insertion_bubble():
  import selection_insertion_bubble
  assert selection_insertion_bubble.selection_sort([15, 37, 17, 34, 5, 45, 22, 26, 6, 41],10) == [5, 6, 15, 17, 22, 26, 34, 37, 41, 45]
  assert selection_insertion_bubble.insertion_sort([15, 37, 17, 34, 5, 45, 22, 26, 6, 41]) == [5, 6, 15, 17, 22, 26, 34, 37, 41, 45]
  assert selection_insertion_bubble.bubble_sort([15, 37, 17, 34, 5, 45, 22, 26, 6, 41]) == [5, 6, 15, 17, 22, 26, 34, 37, 41, 45]