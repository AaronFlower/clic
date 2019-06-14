## Clic

> Clic is a tool for c/c++ Development

### Requirements

First, you should clone [google/googletest] in your local machine.

- [google/googletest](https://github.com/google/googletest)
- CMake

### Install

### How to use

After googletest installed, you need to export a environment `GTEST_PATH` in your bash config file (e.g `.bashrc, .zshrc`, etc).

```bash
$ clic my-cpp
$ cd my-cpp
$ tree
```

If you don't want to export the `GTEST_PATH` environment,  you can specify the path in the same command as follows:

```c
$ GTEST_PATH=/path/to/cloned/googletest clic my-new-app
$ cd my-new-app
$ tree
```

### Todos

- [ ] ctest
