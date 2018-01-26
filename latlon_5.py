#!/usr/bin/python
#latlon_5.py

import re #do this to downoad the function regular expression

def decimalat(DegString): #functions must be defined before you can use it (def=define)
	SearchStr='(\d+) ([\d\.]+) (\w)' #this requires that you open the InFile later, because they belong together
#	Result=re.search(SearchStr,ElementList[2]) #the result should search for ElementList[2] which the program has to find
	Result=re.search(SearchStr,DegString)

#	DegreeString=Result.group(1) #(1) means the same like $1 in jEdit
#	MinuteString=Result.group(2)
#	Compass=Result.group(3)
	print Result.group(2)
	Degrees=float(Result.group(1))
	Minutes=float(Result.group(2))
	Compass=Result.group(3).upper()

	DecimalDegree = Degrees + Minutes/60 #/60 because of sec. & hours

	if Compass=='S' or Compass=='W': #south and west
		DecimalDegree=-DecimalDegree
	return DecimalDegree #return means, which function it has to send back, has to stand before the for loop & before the program is readed

InFileName='Marrus_claudanielis.txt' #now open the file
OutFileName='dec_'+InFileName
WriteOutFile= True
InFile=open(InFileName,'r')
HeaderLine='dive\tdepth\tlatitude\tlongitude\tdate\tcomment'
print HeaderLine #write the Headliner for the list you are building #all in all you this script copys choosen parts out of the different ElementLists and paste them into a new list/table
if WriteOutFile:
	OutFile=open(OutFileName,'w')
	OutFile.write(HeaderLine+'\n')
LineNumber=0
for Line in InFile: #read files (ElementLists) in a for loop with if statements... if it like... than...and than add the placemarkers &after that LineNumber+=1 to start again at the beginning.
	if LineNumber>0:
		Line=Line.strip('\n')
		ElementList=Line.split('\t')
		Dive=ElementList[0] #here you define what you copy and paste (s.a.)
		Date=ElementList[1]
		Depth=ElementList[4]
		Comment=ElementList[5]
		print "Look here", ElementList[2], ElementList[3]
		LatDegrees=decimalat(ElementList[2]) #define Latitude and Longitude, so that the program can recognize them
		LonDegrees=decimalat(ElementList[3])
		print "Look here after decimalar", LatDegrees, LonDegrees
		print 'Lat: %f, Lon:%f' %(LatDegrees,LonDegrees) #print for check

		PlacemarkString='''
<Placemark>
	<name>Marrus - %s</name>
	<description>%s</description>
	<Point>
		<altitudeMode>absolute</altitudeMode>
		<coordinates>%f, %f, -%s</coordiantes>
	<Point>
</Placemark>''' % (Dive,Line,LonDegrees,LatDegrees,Depth)
		if WriteOutFile:
			OutFile.write(PlacemarkString)
		else:
			print PlacemarkString
	LineNumber+=1
InFile.close()
if WriteOutFile:
	print'Saved',LineNumber,'records form',InFileName,'as',\
		OutFileName
	OutFile.write('\n</Documents>\n</kml>\n')
	OutFile.close()
else:
	print '\n</Document>\n</kml>\n'

#here you modify the latlon_4.py script, so that it can be used for Google Earth
#you want translate in KML = Keyhole Markup Language
#because not all data are KML yet, you should change them all & put all data from the inputfile into the outputfile
#but the placemarker is used to generate a header
#so that you now generate headeer & fooder within a loop
#the resulting string also has to include the line-endings \n
#as you see in the following you can insert all 5 values at once, what is faster & shorter than do it one by one
#you parse strings of other files into your list
