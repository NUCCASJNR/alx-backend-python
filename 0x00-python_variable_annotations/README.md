## 0x00-python_variable_annotations

## Advanced Python

- Python is a dynamically-typed language. That means that variable types are dynamically set at run-time, upon assignment of a value to a variable.

- For example, in

```bash
def fn(a, b):
    return a + b
```

- The types of a and b are not known at build-time, only when a and b are assigned values at run-time.

- Hence, calling

```bash
fn("a", 1)
```

- somewhere in your code will not raise an exception until the code is actually executed and the function is called:

```bash
fn("a", 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

- In Python 3, type annotations do not change this. Python is still a dynamically-typed language. Type annotations serve the following purpose:

- Code documentation: thanks to them, a developer reading type-annotated code (his own or someone else’s) will know exactly what type each variables is supposed to be. This helps reduce bugs and exceptions and accelerate the development cycle.

- Linting and validation: code editors and continuous integration (CI) pipelines can be configured to automatically validate type-annotated code at build-time and catch bugs before they make it to production.

![image](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.reddit.com%2Fr%2Fthe_donaldbailey%2F&psig=AOvVaw2_JiG_x5XtMv7ATZ7BrqIw&ust=1691144448152000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCNDt65OiwIADFQAAAAAdAAAAABAE)
