
- `__eq__` specific method defines the behavior of the class for the `==` operator

- `__hash__` python uses to control the behavior of objects when you add them to sets or use them as dict keys.[docs](https://oreil.ly/YUzg5)

> [!IMPORTANT]
> you shouldb't modify `__hash__` without also modifying `__eq__`. reading is suggested [python_hashes_and_equality](https://oreil.ly/vxkgX)