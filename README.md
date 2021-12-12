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



## 3. Package and Distribution building 

- #### Method 1 using setup.py

  - **How to build:** 
    
    > 1. Install build package #py -m pip install --upgrade build     
    > 2. create build: #python setup.py sdist bdist_wheel


- #### Method 2 using setup.py and setup.cfg(using metadata)

   - **How to build:**     
     
     > 1.create build: #python setup.py sdist bdist_wheel
     
   - **Code:setup.py**      
   ```python
    setuptools.setup()          
    import setuptools
   ```

    - **Code:setup.cfg**             
    ```
   [metadata]
   name = pkgTest
   version = 0.0.1
   author = ChenChih.Lee
   author_email=jacklee26@gmail.com
   description = My first Python Hello world library
   long_description = file: README.md
   long_description_content_type = text/markdown
   url = https://github.com/chenchih/PackageTest
   license = MIT
   classifiers = 
   Development Status :: 1 - Planning
   Intended Audience :: Developers
   Programming Language :: Python :: 3
   Operating System :: Unix
   Operating System :: MacOS :: MacOS X
   Operating System :: Microsoft :: Windows
   [options]
   include_package_data = True
   packages = find:
   install_requires = selenium
   [options.entry_points]
   console_scripts =
       helloworld-cli = pkgTest.helloworld:hellotest
   [options.package_data]
   * =
       *.xml
       *.txt
    ```

- #### Method 3 using myproject.toml and setup.cfg(using metadata)

  - **How to build:**
    
     > 1. Install build package #py -m pip install --upgrade build     
     > 2. Create build: #python -m build     >
     > 3. install it           
     >    #pip install .    
     >    OR 
     >    #pip install package name

   -  **Code:** myproject.toml

    ```
    [build-system]
    requires = [
        "setuptools>=42",
        "wheel"
    ]
    build-backend = "setuptools.build_meta"
    ```
