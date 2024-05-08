# This project is about impelementing different caching replacement policies such as LIFO, FIFO, LRU, and MRU

- **pycodestyle used as a code formatter.**
- **All py files are executable.**
- **Modules and functions well documented.**


## Tasks
### [0. Basic dictionary](https://github.com/ehabsmh/alx-backend/tree/main/0x01-caching/0-basic_cache.py)
Implements a class `BasicCache` that inherits from `BaseCaching` and is a caching system:

- must use `self.cache_data` - dictionary from the parent class `BaseCaching`
- This caching system doesn’t have limit
- `def put(self, key, item):`
    - Must assign to the dictionary self.cache_data the `item` value for the key `key`.
    - If `key` or `item` is `None`, this method should not do anything.
- `def get(self, key):`
    - Must return the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.

---

### [1. FIFO caching](https://github.com/ehabsmh/alx-backend/tree/main/0x01-caching/1-fifo_cache.py)
Implements a class `FIFOCache` that inherits from `BaseCaching` and is a caching system:

- Must use `self.cache_data` - dictionary from the parent class `BaseCaching`
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`
- `def put(self, key, item):`
    - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
    - If `key` or `item` is `None`, this method should not do anything.
    - If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
        - You must discard the first item put in cache (FIFO algorithm)
        - You must print `DISCARD:` with the `key` discarded and following by a new line
- `def get(self, key):`
    - Must return the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.

---

### [2. LIFO Caching](https://github.com/ehabsmh/alx-backend/tree/main/0x01-caching/2-lifo_cache.py)
Implements a class `LIFOCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`
- `def put(self, key, item):`
    - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
    - If `key` or `item` is `None`, this method should not do anything.
    - If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
        - You must discard the last item put in cache (LIFO algorithm)
        - You must print `DISCARD:` with the `key` discarded and following by a new line
- `def get(self, key):`
    - Must return the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.

---

### [3. LRU Caching](https://github.com/ehabsmh/alx-backend/tree/main/0x01-caching/3-lru_cache.py)
Create a class `LRUCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`
- `def put(self, key, item):`
    - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
    - If `key` or `item` is `None`, this method should not do anything.
    - If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
        - you must discard the least recently used item (LRU algorithm)
        - you must print `DISCARD:` with the `key` discarded and following by a new line
- `def get(self, key):`
    - Must return the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.
