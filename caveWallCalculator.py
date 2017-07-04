import viz
import vizact
import vizinfo
import vizinput

centerInput = vizinput.input('Enter the distance between front and center:')
wallHeight = vizinput.input('Enter the wall height:')
wallWidth = vizinput.input('Enter the wall width:')

a = float(wallHeight)
b = float(wallWidth)
c = float(centerInput)
 
if c == 0.0:
	#################
	####FrontWall####
	#################

	#upperLeft
	upLeFroX = -(b / 2)
	upLeFroY = a
	upLeFroZ = b / 2
	#upperLeftFro = [upLeFroX, upLeFroY, upLeFroZ]
	#print upperLeftFro

	#upperRight
	upRiFroX = b / 2
	upRiFroY = a
	upRiFroZ = b / 2
	#upperRightFro = [upRiFroX, upRiFroY, upRiFroZ]
	#print upperRightFro

	#lowerLeft
	loLeFroX = -(b / 2)
	loLeFroY = 0.0
	loLeFroZ = b / 2
	#lowerLeftFro = [loLeFroX, loLeFroY, loLeFroZ]
	#print lowerLeftFro

	#lowerRight
	loRiFroX = b / 2
	loRiFroY = 0.0
	loRiFroZ = b / 2
	#lowerRightFro = [loRiFroX, loRiFroY, loRiFroZ]
	#print lowerRightFro

	################
	####LeftWall####
	################

	#upperLeft
	upLeLefX = -(b / 2)
	upLeLefY = a
	upLeLefZ = -(b / 2)
	#upperLeftLef = [upLeLefX, upLeLefY, upLeLefZ]
	#print upperLeftLef

	#upperRight
	upRiLefX = -(b / 2)
	upRiLefY = a
	upRiLefZ = b / 2
	#upperRightLef = [upRiLefX, upRiLefY, upRiLefZ]
	#print upperRightLef
	
	#lowerLeft
	loLeLefX = -(b / 2)
	loLeLefY = 0.0
	loLeLefZ = -(b / 2)
	#lowerLeftLef = [loLeLefX, loLeLefY, loLeLefZ]
	#print lowerLeftLef
	
	#lowerRight
	loRiLefX = -(b / 2)
	loRiLefY = 0.0
	loRiLefZ = b / 2
	#lowerRightLef = [loRiLefX, loRiLefY, loRiLefZ]
	#print lowerRightLef
	
	##################
	####BottomWall####
	##################

	#upperLeft
	upLeBotX = -(b / 2)
	upLeBotY = 0.0
	upLeBotZ = b / 2
	#upperLeftBot = [upLeBotX, upLeBotY, upLeBotZ]
	#print upperLeftBot

	#upperRight
	upRiBotX = b / 2
	upRiBotY = 0.0
	upRiBotZ = b / 2
	#upperRightBot = [upRiBotX, upRiBotY, upRiBotZ]
	#print upperRightBot

	#lowerLeft
	loLeBotX = -(b / 2)
	loLeBotY = 0.0
	loLeBotZ = a
	#lowerLeftBot = [loLeBotX, loLeBotY, loLeBotZ]
	#print lowerLeftBot

	#lowerRight
	loRiBotX = b / 2
	loRiBotY = 0.0
	loRiBotZ = a
	#lowerRightBot = [loRiBotX, loRiBotY, loRiBotZ]
	#print lowerRightBot

	#################
	####RightWall####
	#################
	
	#upperLeft
	upLeRigX = b / 2
	upLeRigY = a
	upLeRigZ = b / 2
	#upperLeftRig = [upLeRigX, upLeRigY, upLeRigZ]
	#print upperLeftRig

	#upperRight
	upRiRigX = b / 2
	upRiRigY = a
	upRiRigZ = -(b / 2)
	#upperRightRig = [upRiRigX, upRiRigY, upRiRigZ]
	#print upperRightRig

	#lowerLeft
	loLeRigX = b / 2
	loLeRigY = 0.0
	loLeRigZ = b / 2
	#lowerLeftRig = [loLeRigX, loLeRigY, loLeRigZ]
	#print lowerLeftRig

	#lowerRight
	loRiRigX = b / 2
	loRiRigY = 0.0
	loRiRigZ = -(b / 2)
	#lowerRightRig = [loRiRigX, loRiRigY, loRiRigZ]
	#print lowerRightRig


elif c >= 0.0:
	#################
	####FrontWall####
	#################

	#upperLeft
	upLeFroX = -(b / 2)
	upLeFroY = a
	upLeFroZ = c
	#upperLeftFro = [upLeFroX, upLeFroY, upLeFroZ]
	#print upperLeftFro

	#upperRight
	upRiFroX = b / 2
	upRiFroY = a
	upRiFroZ = c
	#upperRightFro = [upRiFroX, upRiFroY, upRiFroZ]
	#print upperRightFro

	#lowerLeft
	loLeFroX = -(b / 2)
	loLeFroY = 0.0
	loLeFroZ = c
	#lowerLeftFro = [loLeFroX, loLeFroY, loLeFroZ]
	#print lowerLeftFro

	#lowerRight
	loRiFroX = b / 2
	loRiFroY = 0.0
	loRiFroZ = c
	#lowerRightFro = [loRiFroX, loRiFroY, loRiFroZ]
	#print lowerRightFro

	################
	####LeftWall####
	################

	#upperLeft
	upLeLefX = -(b / 2)
	upLeLefY = a
	upLeLefZ = -(b - c)
	#upperLeftLef = [upLeLefX, upLeLefY, upLeLefZ]
	#print upperLeftLef

	#upperRight
	upRiLefX = -(b / 2)
	upRiLefY = a
	upRiLefZ = c
	#upperRightLef = [upRiLefX, upRiLefY, upRiLefZ]
	#print upperRightLef
	
	#lowerLeft
	loLeLefX = -(b / 2)
	loLeLefY = 0.0
	loLeLefZ = -(b - c)
	#lowerLeftLef = [loLeLefX, loLeLefY, loLeLefZ]
	#print lowerLeftLef
	
	#lowerRight
	loRiLefX = -(b / 2)
	loRiLefY = 0.0
	loRiLefZ = c
	#lowerRightLef = [loRiLefX, loRiLefY, loRiLefZ]
	#print lowerRightLef
	
	##################
	####BottomWall####
	##################

	#upperLeft
	upLeBotX = -(b / 2)
	upLeBotY = 0.0
	upLeBotZ = c
	#upperLeftBot = [upLeBotX, upLeBotY, upLeBotZ]
	#print upperLeftBot

	#upperRight
	upRiBotX = b / 2
	upRiBotY = 0.0
	upRiBotZ = c
	#upperRightBot = [upRiBotX, upRiBotY, upRiBotZ]
	#print upperRightBot

	#lowerLeft
	loLeBotX = -(b / 2)
	loLeBotY = 0.0
	loLeBotZ = a
	#lowerLeftBot = [loLeBotX, loLeBotY, loLeBotZ]
	#print lowerLeftBot

	#lowerRight
	loRiBotX = b / 2
	loRiBotY = 0.0
	loRiBotZ = a
	#lowerRightBot = [loRiBotX, loRiBotY, loRiBotZ]
	#print lowerRightBot

	#################
	####RightWall####
	#################
	
	#upperLeft
	upLeRigX = b / 2
	upLeRigY = a
	upLeRigZ = c
	#upperLeftRig = [upLeRigX, upLeRigY, upLeRigZ]
	#print upperLeftRig

	#upperRight
	upRiRigX = b / 2
	upRiRigY = a
	upRiRigZ = -(b -c)
	#upperRightRig = [upRiRigX, upRiRigY, upRiRigZ]
	#print upperRightRig

	#lowerLeft
	loLeRigX = b / 2
	loLeRigY = 0.0
	loLeRigZ = c
	#lowerLeftRig = [loLeRigX, loLeRigY, loLeRigZ]
	#print lowerLeftRig

	#lowerRight
	loRiRigX = b / 2
	loRiRigY = 0.0
	loRiRigZ = -(b - c)
	#lowerRightRig = [loRiRigX, loRiRigY, loRiRigZ]
	#print lowerRightRig

	

textFile = open('//VRLOGIC/backoffice/Projekte/wordviz_dev_lab/caveWallCalculator/cave_settings.txt','w')
textFile.write("<vizcave>\n")
textFile.write("<farPlane>-1.000000</farPlane>\n")
textFile.write("<nearPlane>0.100000</nearPlane>\n")
textFile.write("<wall>\n")
textFile.write("<name>Front Wall</name>\n")
textFile.write("<mask>2</mask>\n")
textFile.write("<upperLeft>"+ str(upLeFroX) + " " + str(upLeFroY) + " " + str(upLeFroZ) + " " + "</upperLeft>\n")
textFile.write("<upperRight>"+ str(upRiFroX) + " " +  str(upRiFroY) + " " +  str(upRiFroZ) + " " +  "</upperRight>\n")
textFile.write("<lowerLeft>"+ str(loLeFroX) + " " +  str(loLeFroY) + " " +  str(loLeFroZ) + " " +  "</lowerLeft>\n")
textFile.write("<lowerRight>"+ str(loRiFroX) + " " +  str(loRiFroY) + " " +  str(loRiFroZ) + " " +  "</lowerRight>\n")
textFile.write("</wall>\n")
textFile.write("<wall>\n")
textFile.write("<name>Left Wall</name>\n")
textFile.write("<mask>4</mask>\n")
textFile.write("<upperLeft>"+ str(upLeLefX) + " " +  str(upLeLefY) + " " +  str(upLeLefZ) + " " +  "</upperLeft>\n")
textFile.write("<upperRight>"+ str(upRiLefX) + " " +  str(upRiLefY) + " " +  str(upRiLefZ) + " " +  "</upperRight>\n")
textFile.write("<lowerLeft>"+ str(loLeLefX) + " " +  str(loLeLefY) + " " +  str(loLeLefZ) + " " +  "</lowerLeft>\n")
textFile.write("<lowerRight>"+ str(loRiLefX) + " " +  str(loRiLefY) + " " +  str(loRiLefZ) + " " +  "</lowerRight>\n")
textFile.write("</wall>\n")
textFile.write("<wall>\n")
textFile.write("<name>Bottom Wall</name>\n")
textFile.write("<mask>8<mask>\n")
textFile.write("<upperLeft>"+ str(upLeBotX) + " " +  str(upLeBotY) + " " +  str(upLeBotZ) + " " +  "</upperLeft>\n")
textFile.write("<upperRight>"+ str(upRiBotX) + " " +  str(upRiBotY) + " " +  str(upRiBotZ) + " " +  "</upperRight>\n")
textFile.write("<lowerLeft>"+ str(loLeBotX) + " " +  str(loLeBotY) + " " +  str(loLeBotZ) + " " +  "</lowerLeft>\n")
textFile.write("<lowerRight>"+ str(loRiBotX) + " " +  str(loRiBotY) + " " +  str(loRiBotZ) + " " +  "</lowerRight>\n")
textFile.write("/wall>\n")
textFile.write("<wall>\n")
textFile.write("<name>Rigth Wall</name>\n")
textFile.write("<upperLeft>"+ str(upLeRigX) + " " +  str(upLeRigY) + " " +  str(upLeRigZ) + " " +  "</upperLeft>\n")
textFile.write("<upperRight>"+ str(upRiRigX) + " " +  str(upRiRigY) + " " +  str(upRiRigZ) + " " +  "</upperRight>\n")
textFile.write("<lowerLeft>"+ str(loLeRigX) + " " +  str(loLeRigY) + " " +  str(loLeRigZ) + " " +  "</lowerLeft>\n")
textFile.write("<lowerRight>"+ str(loRiRigX) + " " +  str(loRiRigY) + " " +  str(loRiRigZ) + " " +  "</lowerRight>\n")
textFile.write("</wall>\n")
textFile.write("</vizcave>\n")