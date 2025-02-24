# -*- coding: utf-8 -*-
"""code.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17JDAukz5Ne919BgF8PrmZvVEj-_3A2YA
"""

def count_pre_words(input_line):
  words = input_line.split()
  counts = {}
  result = []

  for el in words:
    result.append(counts.get(el, 0))
    counts[el] = counts.get(el, 0) + 1

  return result