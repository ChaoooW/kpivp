def test_shift_elem():
  import shift_array
  assert shift_array.shift_elem([0,  1,  2,  3,  4,  5,  6,  7,  8,  9], 10) == [1,  2,  3,  4,  5,  6,  7,  8,  9,  0]
  assert shift_array.shift_elem([1,  2,  3,  4,  5,  6,  7,  8,  9,  0], 10) == [2,  3,  4,  5,  6,  7,  8,  9, 0, 1]
  assert shift_array.shift_elem([2,  3,  4,  5,  6,  7,  8,  9, 0, 1], 10) == [3,  4,  5,  6,  7,  8,  9, 0, 1, 2]