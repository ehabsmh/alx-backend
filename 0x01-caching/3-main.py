#!/usr/bin/python3
""" 3-main """
LRUCache = __import__('3-lru_cache').LRUCache

my_cache = LRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache() # A - B - C - D
print(my_cache.get("B")) # World
my_cache.put("E", "Battery") # DISCARD: A
my_cache.print_cache() # B - C - D - E
my_cache.put("C", "Street")
my_cache.print_cache() # B - C - D - E
print(my_cache.get("A")) # None
print(my_cache.get("B")) # World
print(my_cache.get("C")) # Street
my_cache.put("F", "Mission") # DISCARD: D
my_cache.print_cache() # B - C - E - F
my_cache.put("G", "San Francisco") # DISCARD: E
my_cache.print_cache() # B - C - F - G
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()
