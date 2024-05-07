# This project is about impelementing different caching mechanisms such as LIFO, FIFO, LRU, and MRU

**- pycodestyle used as a code formatter**
**- All py files are executable**
**- Modules and functions well documented**


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