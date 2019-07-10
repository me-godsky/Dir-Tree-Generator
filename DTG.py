import os
import colored
from colored import stylize
import argparse
from PIL import ImageDraw, ImageFont, Image

 
z = 10


def check( image, path, x , a  ):

	try :
		global z	
		for i in os.listdir(path):
			z = z + 10
			if os.path.isdir(os.path.join(path,i)):
			
				x = x - 1
				m = "|   "*(a-1) + "|" + "__"*a 
				(y,z) = (10 ,z)
				color1 = 'rgb(250,0,0)'
				color2 = 'rgb(0,0,0)' 
				i = "    "*(a-1) + " " + "  "*a + i
				image.text((y , z), m, fill=color2)
				image.text((y , z), i, fill=color1)

				if x > 0 :	
					i = i.split("    "*(a-1) + " " + "  "*a )[-1]
					check(image, os.path.join(path,i), x ,a=a+1)
					
	
			elif os.path.isfile(os.path.join(path,i)):
				
				m = "|   "*(a-1) + "|" + "__"*a
				(y,z) = (10 , z)
				color1 = 'rgb(0,250,0)'
				color2 = 'rgb(0,0,0)'
				i = "    "*(a-1) + " " + "  "*a + i
				image.text((y , z), m, fill=color2)
				image.text((y , z), i, fill=color1)
				

			else :
				print("unknown filetype")
			
			
	except (KeyboardInterrupt, SystemExit):
		print(" There was an error while processng ")

	except KeyError:
		print("Key Error :(")



def main():
	try :		
		parser = argparse.ArgumentParser()
		parser.add_argument('-p', '--path', action = 'store', dest = 'path', help= 'Path to destination directory')
		parser.add_argument('-d', '--depth',type = int, action = 'store' , dest = 'depth' , help = 'Depth for dir traversing')
		parser.add_argument('-l', '--length', action = 'store', dest = 'length', help= 'Length[ in pixels ] of the file')
		parser.add_argument('-b', '--breadth', action = 'store', dest = 'breadth', help= 'Breadth[ in pixels ] of the file')
		parser.add_argument('-f', '--filename', action = 'store', dest = 'filename', help= 'Filename [ with extension ]')
		results = parser.parse_args()
		c = os.getcwd()
		os.chdir(c + '/Images')
		i = Image.new('RGB', (int(results.length), int(results.breadth)), color = (255, 255, 255))
		image = ImageDraw.Draw(i)
		image.text((10 , z), results.path.split('/')[-2], fill='rgb(250,0,0)')
		check(image, results.path , results.depth, 1)	
		i.save(results.filename)	
		os.chdir(c)
		print('''


		File Exported Successfully!

''')

	except (KeyboardInterrupt, SystemExit):
		print(" There was an error while processng ")

	except KeyError:
		print("Key Error :(")

	except :
		print('''
		***********************   Warning   ************************
		*							   *
		*		All options are mandatory!		   *
		*							   *
		************************************************************

Usage :

	python3 DTG.py -p <path of dir traversal> -d <depth of traversal> -l <length in pixels of image> -b <breadth in pixels of image> -f <filename>
							
										OR

	python3 DTG.py --path <path of dir traversal> --depth <depth of traversal> --length <length in pixels of image> --breadth <breadth in pixels of image> --filename <filename>
Example :

	python3 DTG.py -p /home/godsky/Desktop/ -d 4 -l 800 -b 1200 -f new.png
''')
		if not results.path:
			print('''        
		
	-------> Specify the path to destination directory!
''')
			pass
		elif not results.depth:
			print('''

	-------> Specify the depth of dir traversal!")
''')
			pass
		elif not results.length:
			print('''

	-------> Specify the length of image in pixels!")
''')
			pass
		elif not results.breadth:
			print('''

	-------> Specify the breadth of image in pixels!")
''')
			pass
		elif not results.filename:
			print('''

	-------> Specify the name of new image file!")
''')
			pass

if __name__ == '__main__' :
	main()
