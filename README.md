# Dir-Tree-Generator
Directory Tree Generator tool 

This tool is designed for better view of Subdirectories and files in a proper format such that an image is created with user defined size.

## Features :

- Output in the form of an image. 
- User defined size of image.
- User can provide depth upto which the traversal of dirs should be done by tool. 
- Sub-dirs are represented by red and files by green colour.

## Usage :

**python3 DTG.py -p [path of dir traversal] -d [depth of traversal] -l [length in pixels of image] -b [breadth in pixels of image] -f [filename]**
							
OR

**python3 DTG.py --path [path of dir traversal] --depth [depth of traversal] --length [length in pixels of image] --breadth [breadth in pixels of image] --filename [filename]**
  
### Example :

	python3 DTG.py -p /home/godsky/Desktop/ -d 4 -l 800 -b 1200 -f new.png
