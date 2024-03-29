from typing import List


class Metadata:
    def __init__(self, limit: int, offset: int, total: int):
        self.limit = limit
        self.offset = offset
        self.total = total


class ListWrapper:
    def __init__(self, metadata: Metadata, items: List[any]):
        self.metadata = metadata
        self.items = items
