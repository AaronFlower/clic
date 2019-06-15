## Clic

> A  cli tool for c/c++ development.

### Requirements

First, you should clone [google/googletest] and install [CMake](https://cmake.org/) in your local machine.

- [google/googletest](https://github.com/google/googletest)
- [CMake](https://cmake.org/)

### Install

```bash
$ pip install clic
```

### How to use

After googletest installed, you need to export a environment `GTEST_PATH` in your bash config file (e.g `.bashrc, .zshrc`, etc).

```bash
$ clic mycpp
$ cd mycpp

$ tree -L 1
.
├── CMakeLists.txt
├── build
├── lib
├── solution.h
└── test.cpp

2 directories, 3 files

$ cd build
$ cmake .. && make
$ ./mycpp

❯ ./mycpp
Running main() from ~/mycpp/lib/googletest/googletest/src/gtest_main.cc
[==========] Running 1 test from 1 test suite.
[----------] Global test environment set-up.
[----------] 1 test from test
[ RUN      ] test.INIT
Hello mycpp
[       OK ] test.INIT (0 ms)
[----------] 1 test from test (0 ms total)

[----------] Global test environment tear-down
[==========] 1 test from 1 test suite ran. (0 ms total)
[  PASSED  ] 1 test.
```

If you don't want to export the `GTEST_PATH` environment,  you can specify the path in the same command as follows:

```c
$ GTEST_PATH=/path/to/cloned/googletest clic my-new-app
$ cd my-new-app
```

Now, Enjoy your simple c/c++ project. 😉
