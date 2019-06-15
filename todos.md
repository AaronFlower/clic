## Todos

- [ ] tests

### How to develop

1. build and test locally

```bash
$ python3 setup.py bdist_wheel
$ pip3 install dist/clic-0.1.2-py3-none-any.whl
```

2. publish to Pypi

```bash
# change the `setup.py` version
$ python3 setup.py bdist_wheel
$ python3 -m twine upload dist/*
Enter your username: AaronFlower
Enter your password:
Uploading distributions to https://upload.pypi.org/legacy/
Uploading clic-0.1.2-py3-none-any.whl
100%|██████████████████████████████████████████████████████████████| 9.44k/9.44k [00:03<00:00, 3.10kB/s]
```

### References

1. [Getting Started With Testing in Python](https://realpython.com/python-testing/)
2. [Package to PyPI](https://realpython.com/pypi-publish-python-package/#preparing-your-package-for-publication)
