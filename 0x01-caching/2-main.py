#!/usr/bin/python3
""" 2-main """
LIFOCache = __import__('2-lifo_cache').LIFOCache

my_cache = LIFOCache()
my_cache.put("A", "Hello") # 1
my_cache.put("B", "World") # 2
my_cache.put("C", "Holberton") # 3
my_cache.put("D", "School") # 4
my_cache.print_cache() # A - B - C - D
my_cache.put("E", "Battery")  # DISCARD: D
my_cache.print_cache() # A - B - C - E
my_cache.put("C", "Street") # DISCARD C
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
