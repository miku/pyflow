from typing import TypeVar, Generic, Iterable, Iterator

# a) We know that Derived can be used anywhere Base can - does that mean that List[Derived] can be used wherever List[Base] can?
# b) Maybe it's the reverse direction and now List[Base] can be used wherever List[Derived] can

# a) covariance
# b) contravariance

T_co = TypeVar('T_co', covariant=True) 

class ImmutableList(Generic[T_co]): # allow 
    def __init__(self, items: Iterable[T_co]) -> None: ...
    def __iter__(self) -> Iterator[T_co]: ... # type: ignore
    ...

class Employee: ...

class Manager(Employee): ...

def list_employees(emps: ImmutableList[Employee]) -> None:
    for emp in emps:
        ...

mgrs = ImmutableList([Manager()])  # type: ImmutableList[Manager]
list_employees(mgrs)  # OK