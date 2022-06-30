# diceFpy (random dice generator for python)
Random dice generator for python, or diceFpy, is an terminal based  random 
dice generator made with python. It was made in a linux environment but 
should work on all platform (window or macOs). It as two option (-n or -h).
and can take at most 2 terminal argument. The implementations is pretty basic
but the functionality is there.

This is an open source project and you can use it or/and change it hovewer you like.

## table of content
1. installation
2. usage
3. option
4. testing
5. license

## Installation
In order to install this software you need to download this repositery.
You can use the user interface provided by github or an terminal command like
curl (or anything similar).

## Usage
You can either use diceFpy with the python interpreter (this will work anywere).
Or by using the dot syntax (this will work in unix related environment).
Keep in mind that for the interpret you need to be in the same folder as the
source code.

```bash
reader@folder:python3 diceFpy -n 2
[1]
[2]
reader@folder:./diceFpy -n 2
[4]
[11]
```

# Option
You can use and set option using the -[option] syntax.

```bash
	-h 		# this will show the usage/help page of the program
	-n [integer]	# this will show you the giving ammount of dice

```

## Testing
The test_dicepy.py file is the source code for all the test of this application.
The test test the main functionality of diceFpy. It also test all the function
used in diceFpy. In order to excute the test you need to have __pytest__ install.
All the test are inside the test file

``` bash
reader@folder:pytest -v test_dicefpy.py	# how to run the tests
```

## License
This project use the GPL-2.0 license.

