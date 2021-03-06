import dataclasses
from typing import Any, List, Optional

from .operation import Operation


@dataclasses.dataclass
class Job(object):
    ops: Optional[List[Operation]] = None
    name: str = 'Job'
    __ATTR_NAMES = ('processed_by', 'r', 'p', 'q')

    def __iter__(self):
        self.__i = 0
        return self

    def __getitem__(self, idx: int):
        return self.ops[idx]

    def __len__(self):
        return len(self.ops)

    def __next__(self):
        if self.__i == len(self):
            raise StopIteration
        op = self.ops[self.__i]
        self.__i += 1
        return op

    def append(self, op: Operation) -> None:
        if self.ops is None:
            self.ops = [op]
        else:
            self.ops.append(op)

    def attrtolist(self, attr_name: str = 'p') -> List[Any]:
        err_msg = f"invalid attribute name: {attr_name}. Choose from {self.__ATTR_NAMES}"
        assert attr_name in self.__ATTR_NAMES, err_msg
        return [getattr(op, attr_name) for op in self]

    def setattr(self, values: Any, attr_name: str = 'p') -> None:
        err_msg = f"invalid attribute name: {attr_name}. Choose from {self.__ATTR_NAMES}"
        assert attr_name in self.__ATTR_NAMES, err_msg
        for op, val in zip(self, values):
            setattr(op, attr_name, val)
