#!/usr/bin/env python
'''

For every line, please add a comment describing what it does. 

Try to describe each line within the context of the program as a whole, rather than just mechanically

Feel free to alter the parameters to see how things change. That can be a great way to be able to intuit what is supposed to be happening

I will do the first two lines for you as an example


'''
import sys, pygame	# imports the sys and pygame modules so they can be used in this program
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' # requires that the Python 3.4 (or higher version) interpreter is being used; i.e., not compatible with Python 2

screen_size = (800,600) #Sets the size of the background scene on an x and y-axis by pixels. So an 800x600 will appear
FPS = 60 #defining FPS as integer 60.

def main(): #Defining the function main()
	pygame.init() #The init function will tell it to run the program right away
	screen = pygame.display.set_mode(screen_size) #Displays the screen defined above.
	clock = pygame.time.Clock() #Rate at which the program is run

	while True: #While loop
		clock.tick(FPS)	#Sets the frame rate so that it doesn't exceed 60 frames per second
		screen.fill((0,0,0)) #color of the screen, in this case it will be black.

		for event in pygame.event.get():
			if event.type == pygame.QUIT: #Condition of if the event is quit.
				pygame.quit() #quits the pyGame module
				sys.exit(0) #exits the program at a system level.

		pygame.display.flip() #The picture on the screen that is set to change is automatically flipped all at once on the screen

if __name__ == '__main__': # If you recall as a .py file, it will run the program, if it is recalled as a module (imported) it won't automatically run.
	main() #run the function