#Python 2.7.12 (default, Nov 19 2016, 06:48:10)
#[GCC 5.4.0 20160609] on linux2
#Type "help", "copyright", "credits" or "license" for more information.

#If you are in a different directory, you can manually add a search path location using the sys module with sys.path.

import subtract
result = subtract.subtract(10, 5)
result

print(result)
#5


#In order for Python to recognize it as a Python package, just create a __init__.py file in this directory.
#The __init__.py file can often be an empty file. In the same example as the subtract.py file, if you were to create a directory called math_stuff and create a __init__.py file:
#The way you will now refer to the module will need to include the package name using the dot notation, for example, math_stuff.subtract:
    
#echou@pythonicNeteng:~/Master_Python_Networking/Chapter1$ mkdir math_stuff
#echou@pythonicNeteng:~/Master_Python_Networking/Chapter1$ touch math_stuff/__init__.py
#echou@pythonicNeteng:~/Master_Python_Networking/Chapter1$ tree
#.
# ├── helloworld.py
# └── math_stuff
#  ├── __init__.py
#  └── subtract.py
#1 directory, 3 files
#echou@pythonicNeteng:~/Master_Python_Networking/Chapter1$

#>>> from math_stuff.subtract import subtract
#>>> result = subtract(10, 5)
#>>> result
#5
#>>>

    