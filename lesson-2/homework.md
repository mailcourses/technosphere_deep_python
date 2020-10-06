# Домашнее задание к лекции №2

## Реализовать LRU cache (least recently used)

Класс должен содержать следующие методы
```python
class ICache:
    def __init__(self, capacity: int=10) -> None:
        pass

    def get(self, key: str) -> str:
        pass

    def set(self, key: str, value: str) -> None:
        pass

    def delete(self, key: str) -> None:
        pass
```
Проверяться работоспособность должна так:
```python
from cache import LRUCache

cache = LRUCache(100)
cache.set('Jesse', 'Pinkman')
cache.set('Walter', 'White')
cache.set('Jesse', 'James')
cache.get('Jesse') # вернёт 'James'
cache.del('Walter')
cache.get('Walter') # вернёт ''
```

## Реализовать класс, отнаследованный от списка, такой, что один список
- Можно вычитать из другого [5, 1, 3] - [1, 2, 7] = [4, -1, -4];
- Можно складывать с другим;
- При неравной длине, дополнять меньший список нулями только на время выполнения операции. Исходные списки не должны изменяться;
- При сравнении списков должна сравниваться сумма элементов списков.
