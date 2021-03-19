# Iot Python Labs

## Lab 4
 - Write tests to lab 3
 - Tests coverage should be 70%
 - Code must be in separate pull request

### Tests coverage:
```
maxrt@macbook:lab4$ coverage report
Name                         Stmts   Miss  Cover
------------------------------------------------
shoes/__init__.py                5      0   100%
shoes/boots.py                   4      0   100%
shoes/flip_flops.py              4      0   100%
shoes/manager/__init__.py        1      0   100%
shoes/manager/manager.py        19      0   100%
shoes/shoes.py                  21      1    95%
shoes/sneakers.py                4      0   100%
shoes/test/__init__.py           0      0   100%
shoes/test/test_find.py         15      0   100%
shoes/test/test_manager.py      15      0   100%
shoes/test/test_shoes.py        20      0   100%
shoes/test/test_sort.py         19      0   100%
shoes/testing/__init__.py        2      0   100%
shoes/testing/test.py           13      8    38%
------------------------------------------------
TOTAL                          142      9    94%
```

### To run tests:
  - Clone/Download lab2 branch
  - Go into repo folder
  - Type `python3 -m unittest`


## Lab 3
### Lab 3 Task
 - Write code to lab 2 task
 - Use python code convention
 - Classes must be in different packets
 - Clonsole interraction must be minimal
 - Code must include only those classes, which are described in class diagram
 - Class attributes/methods and their visibility must coincide with values from class diagram
 - Sorting must be implemented in separate method
 - Code must be uploaded in separate branch as pull request
 - For checking your code, you should create separate class, which contains main method

### To run:
  - Clone/Download lab2 branch
  - Go into repo folder
  - Type `./main.py` or `python3 main.py`

