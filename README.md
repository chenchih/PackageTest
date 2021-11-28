# Test Package 

[![GitHub license](https://img.shields.io/github/license/chenchih/PackageTest)](https://github.com/chenchih/PackageTest/blob/main/LICENSE)


Still on process, not ready for use yet! Currently studying and planning !



## 1. Version

- 0.0.1 inital version
- 0.0.2 update readme.md

## 2. Example and Description
This is a test package, which include these item:
- [x] Calculate Test
- [x] Hello world Test

### Hello World Package
> **Method name**: helloworld

```python
from pkgTest import helloworld as hello
print(hello.hellotest())

# output

```

### calculate Package
> **Method name**: calculate

- #### Calculate  sum of range X value, start to end 

```python
from pkgTest import calculate as cal
result = cal.sumvalue(1,300)
print(result) 
# output
The sum of 1, ~ 300 is: 44850 
```

- ####  Calculator operator with  two value X and Y 
```python
from pkgTest import calculate as cal
cal.add(5,5)
cal.minus(5,5)
cal.multiply(5,5)
cal.divide(5,5)

# output
10 #adding
0  #subtract
25 #multiply
1  #divide
```

