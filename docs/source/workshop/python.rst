======
Python
======

What is Python
--------------

Python is a fun and powerful programming language used in web applications and desktop software. It's used alot as a binding around well-known OSGeo-backed libraries such as GDAL/OGR andGEOS. Key features include:

    * very clear, readable syntax
    * intuitive object orientation
    * exception-based error handling
    * very high level dynamic data types
    * implemented in many languages (classic Python is C/C++ at it's core, but there are Java (Jython) and .NET (IronPython) implementations)

Why it is important/popular
---------------------------

* Well, for starters, it can access \  **tons** \ of OSGeo libraries and software to do workflows programmatically. Some of these include (but are not limited to):
    - PostGIS
    - GDAL/OGR
    - GEOS
    - JTS
    - GeoTools
    - Proj4
    - Mapserver
    - gvSIG

* Its names after Monty Python (the best movie ever)

* It's easy to learn yet very very powerful

Examples
-----------

Getting help::

    >>> help(range)
    Help on built-in function range in module __builtin__:

    range(...)
        range([start,] stop[, step]) -> list of integers
        
        Return a list containing an arithmetic progression of integers.
        range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
        When step is given, it specifies the increment (or decrement).
        For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
        These are exactly the valid indices for a list of 4 elements.


Strings, numbers, lists oh my. The mightiest of Python data types you should know is the List::
    
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


Parsing strings and looping through data::

    >>> # basic for loop
    >>> for i in range(20): print  i
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
 

Running scripts straight from the command-line::

    def buildConnectionString(params):
    """Build a connection string from a dictionary of parameters.

    Returns string."""
    return ";".join(["%s=%s" % (k, v) for k, v in params.items()])

    if __name__ == "__main__":
        myParams = {"server":"mpilgrim", \
                        "database":"master", \
                        "uid":"sa", \
                        "pwd":"secret" \
                        }
        print buildConnectionString(myParams)
