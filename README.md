# ECE654-A1  
[![Build Status](https://travis-ci.com/richard3983/ECE654-A1.svg?token=8FHpB6J7vdRyz684YQz8&branch=main)](https://travis-ci.com/richard3983/ECE654-A1)

Perform two simple analyses on ASTs:
1. There are no identifiers with length equal 13
2. Maximum control structure nesting of 4

## Usage

```
python3 src/main.py --program=path_to_the_program
```

## Demo
Run simple analyses on demo.py:
```
python3 src/main.py --program='src/demo.py'
```
Expected output:
```
There is no identifiers with length equal 13
0 nodes have control structure nesting greater than 4
```