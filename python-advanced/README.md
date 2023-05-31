# Advanced Python

## Context Manager

> context manager is an `object` that defines the `runtime` execution context within the `with` statement.

```python
# Typical context manger syntax
with cotext as ctx:
    # code need to be executed within context.
# within above context all the execution and their
# code cleanup will be done.
# Normal flow begins.
```
The context manager protocol supports below two methods, if you want a class to support the context manager
protocol that need to implement these functions
1. `__enter__()` - set up the object and optionally return the object
2. `__exit__()` - clean up the object
