# Slots

> __slots__ has a mixed reputation in the Python community. On the one hand,
> they are considered to be popular. Lots of people like using them. Others say
> that they are badly understood, tricky to get right, and don't have much of an
> effect unless there are many instances of objects that use them. -- [https://wiki.python.org/moin/UsingSlots](https://wiki.python.org/moin/UsingSlots)

Example: [Snippets/Slots](Snippets/Slots)

* we can save a bit memory, as `__dict__` will not be created

Without slots, we can assign create new attributes on the class. Slots limit this.

## Summary

> Using __slots__ is straightforward. They are a simple, efficient, and safe
> alternative to Python's default method of data access. The only known
> exception is when another object requires access to the __dict__ attribute. 