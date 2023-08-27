## 0x03. Unittests and Integration Tests

![unit test vs. Integration test](./unitttest.jpeg)

- Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.

- The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

- Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

- Integration tests will test interactions between every part of your code.

- Execute your tests with

```bash
$ python -m unittest path/to/test_file.py

```

## For a more verbose output add the -v flag

```bash
$ python -m unittest path/to/test_file.py -v
```

## Resources 
- [unittest — Unit testing framework](https://intranet.alxswe.com/rltoken/a_AEObGK8jeqPtTPmm-gIA)

- [unittest.mock — mock object library](https://intranet.alxswe.com/rltoken/PKetnACd7FfRiU8_kpe5EA)

- [How to mock a readonly property with mock?](https://intranet.alxswe.com/rltoken/2ueVPK1kWZuz525FvZ1v2Q)

- [parameterized](https://intranet.alxswe.com/rltoken/mI7qc3Y42aZ7GTlLXDxgEg)

- [Memoization](https://intranet.alxswe.com/rltoken/x83Hdr54q4Vax5xQ2Z3HSA)

## Required files

- [utils.py](utils.py)

- [client.py](client.py)

- [fixtures.py](fixtures.py)