#do our importing of important stuff
import time
import board
import neopixel
#setting up our colors
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
BLACK = (0, 0, 0)
#set up the pin on our board for output, the number of pixels we are using, 8 per segment, and the number of segments
#we could have done math but someone may make displays with different numbers of segments
pixel_pin = board.GP0
num_pixels = 32
segs = 4
#Initializing our neopixel driver
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

def eseg(segs, color, tval):	#segs = number of digits + 1 for a decimal, color = color, tval = value to display, like 23.5
    tdigs = str(tval)			#tdigs = string representation of value to display so that we can evaluate each digit easier
    tlen = len(tdigs)			#tlen = the length of the string for indexing
    tdec = tdigs.find(".")		#tdec = where is the decimal if any
    if tdec > 0:				#do this bit if there is a decimal
        trdigs = tdigs.split(".")		#Spliting the string at the decimal and pulling out just the digits
        tdigs = trdigs[0]+trdigs[1]		#We already know where to put the decimal back in
        tlen = tlen - 1					#Decrement the length of the string by 1 as we have removed the decimal
    tarry = ["11111010","10000010","11011001","11001011","10100011","01101011","01111011","11000010","11111011","11100011","11111110","10000110","11011101","11001111","10100111","01101111","01111111","11000110","11111111","11100111",]
            #The above is the binary representation of the numbers 0-9 with the '1's telling the program which Neopixel to light up
            #The second set is the digit with the decimal lit.
            #Below is the order of the neopixels
            # 2
            #3 1
            # 8
            #4 7
            # 56
    c = 0							#Initializing our counter
    for i in range(tlen-1,-1,-1):	#Indexing through the string of digits
        t = int(tdigs[i])			#Converting the digit we are working with to an integer
        if i == tdec-1:				#Checking to see if this is the digit with a decimal
            t = t+10				#If so use the appropriate binary sequence
        xt = tarry[t]				#Pull the value from the array
        for z in xt:				#Index through the binary sequence
            if z == "1":			#If it is a 1 set the pixel to the right color
                pixels[c] = color
                c=c+1
            else:
                pixels[c] = BLACK	#Otherwize turn the pixel off
                c=c+1
    time.sleep(.1)					#Obligatory sleep so that we humans can see what is going on
    pixels.show()					#Sending everything we have worked so hard for to the display(s)
v=0						#Initialize a counter
while True:				#Our old friend the while True:
    v=v+1				#Increment our counter
    vx = str(v)			#Convert it to a string
    print(vx)			#Print it to the console so we can follow along
    if v < 3000:		#Check the counter so we can change the color as we count up
        col=GREEN		#Set the first color to green
    else:
        col=YELLOW		#Then yellow
    if v > 6000:
        col = RED		#And finally red
    eseg(5, col, vx)	#Calling our function to display cool color digits.  The code will end with an error when we exceed the number of digits available.


