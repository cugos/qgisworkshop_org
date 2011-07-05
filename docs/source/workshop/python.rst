======
Python
======

What is Python
--------------

Python is a fun and powerful programming language used in web applications and desktop software. It can also be found wrapping OSGeo-backed libraries such as GDAL/OGR, JTS and GEOS. Key features include:

    * very clear, readable syntax
    * intuitive object orientation
    * exception-based error handling
    * very high level dynamic data types
    * implemented in many languages (classic Python is C/C++ at it's core. But there are Java (Jython) and .NET (IronPython) implementations also)

Why it is important/popular
---------------------------

* For our purposes, Python can be used to access \  **tons** \ of OSGeo libraries and software. Then we use Python to write programmatic workflows. Some of this OSGeo software includes but is not limited to:
    - QGIS (or we wouldn't be reading this now)
    - PostGIS
    - GDAL/OGR
    - GEOS
    - JTS
    - GeoTools
    - Proj4
    - Mapserver
    - gvSIG

* It's named after “Monty Python’s Flying Circus”

* It's easy to learn yet very very powerful

Examples
-----------
All the examples below are executed in the Python interpreter. On your Virtual Box install you can access the Python interpreter in two ways -- 1. through QGIS and 2. through the bash shell.

    1. The QGIS Python Console can be started by going to the QGIS file menu and clicking\  ``Plugins --> Python Console`` \
    
    2. The bash shell can be started by holding down\  ``<Cntl>-<ALT>`` \keys and then pressing\  ``t`` \at the same time. Once a new bash shell pops open you just have to type\  ``python`` \into the command prompt and the bash shell magically becomes a Python interpreter. 

Python makes it easy to get help on functions and objects. If a particular variable is giving you trouble then just wrap it in help to display it's meaning (assuming it has one)::

    >>> help(range)
    Help on built-in function range in module __builtin__:

    range(...)
        range([start,] stop[, step]) -> list of integers
        
        Return a list containing an arithmetic progression of integers.
        range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
        When step is given, it specifies the increment (or decrement).
        For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
        These are exactly the valid indices for a list of 4 elements.


Strings, numbers, lists...oh my. The List is the mightiest of Python data types you should know. We can used Lists to store just about anything. Many times records in a database are represented as Lists in Python::
    
    >>> # this is me making a list
    ... a = [10, 50, 123, 1234]
    >>> # Replace some items:
    ... a[0:2] = [1, 12]
    >>> a
    [1, 12, 123, 1234]
    >>> # Remove some:
    ... a[0:2] = []
    >>> a
    [123, 1234]
    >>> # Insert some:
    ... a[1:1] = ['bletch', 'xyzzy']
    >>> a
    [123, 'bletch', 'xyzzy', 1234]
    >>> # Insert (a copy of) itself at the beginning
    >>> a[:0] = a
    >>> a
    [123, 'bletch', 'xyzzy', 1234, 123, 'bletch', 'xyzzy', 1234]
    >>> # Clear the list: replace all items with an empty list
    >>> a[:] = []
    >>> a
    []


An example of parsing strings and looping through data using Lists::

    >>> # basic for loop
    >>> for i in range(1,10): print i
    ... 
    1
    2
    3
    4
    5
    6
    7
    8
    9
    >>> 
    >>> import string
    >>> # sexier loop structure 
    >>> mess = [i for i in string.split("I love maps and I cannot lie"," ")]
    >>> mess
    ['I', 'love', 'maps', 'and', 'I', 'cannot', 'lie']
    >>> really_messy = [i for i in "I love maps and I cannot lie"]
    >>> really_messy
    ['I', ' ', 'l', 'o', 'v', 'e', ' ', 'm', 'a', 'p', 's', ' ', 'a', 'n', 'd', ' ', 'I', ' ', 'c', 'a', 'n', 'n', 'o', 't', ' ', 'l', 'i', 'e']
 

Here's an example you might actually see at work. Let's build database parameters that we want to pass to a function. In this example the first code that executes is\  ``if __name__ == "__main__":`` \. On Linux systems (e.g. Ubuntu) we can execute this script without opening the Python interpreter (Yah!). Copy the code below into a text file and save it as\  ``test.py`` \in some directory. Then open up a bash shell and\  ``cd`` \to that directory and type in the command prompt:\  ``python test.py`` \. Your script will execute and return the following single string:\  ``pwd=secret;database=master;uid=sa;server=gcorradini`` \. Now you try::

    def buildConnectionString(params):
        """Build a connection string from a dictionary of parameters.

        Returns string."""
        return ";".join(["%s=%s" % (k, v) for k, v in params.items()])

    if __name__ == "__main__": 
        myParams = {"server":"gcorradini", \
                        "database":"master", \
                        "uid":"sa", \
                        "pwd":"secret" \
                        }
        print buildConnectionString(myParams)


Here's some good resources to get you started on the Pythonic ninja track:

    `Dive into Python <http://diveintopython.org/toc/index.html>`_

    `How to Think Like a Computer Scientist <http://greenteapress.com/thinkpython/html/index.html>`_

    `The Python Tutorial <http://docs.python.org/tutorial/>`_ \# this is the official one


    

