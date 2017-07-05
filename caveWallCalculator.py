import viz
import math
import vizact
import vizinfo
import vizinput
import vizshape

choice = vizinput.choose("Choose a system to calculate:", ["cave", "powerwall"])

############
####Cave####
############

if choice == 0:
	loop = True
	while loop == True:	
		wallHeight = vizinput.input("Enter the wall height:")
		wallWidth = vizinput.input("Enter the wall width:")

		if wallHeight == "" or wallWidth == "":
			vizinput.message("Error, there was no data recorded. Please enter a value.")
			loop = True
			
		else:
			loop = False
		
	distance = float(wallWidth) / 2

	answerCave1 = vizinput.ask("The recommended tracker origin is "+str(distance)+" meters from the front wall and "+str(distance)+" meters from the left/right wall. Do you want to keep it?")

	if answerCave1 == 1:
		c = 0.0
		centerPoint = [0.0,0.0,0.0]

		a = float(wallHeight)
		b = float(wallWidth)

	else:
		loop = True
		while loop == True:
			centerInput = vizinput.input('Enter the distance between front and tracker origin:')
		
			if centerInput == "":
				vizinput.message("Error, there was no data recorded. Please enter a value.")
				loop = True
				
			else:
				loop = False
				
		a = float(wallHeight)
		b = float(wallWidth)
		c = float(centerInput)
		
		centerTemp = (b / 2) - c
		centerPoint = [0.0, centerTemp, 0.0]

	if c == 0.0:
		#################
		####FrontWall####
		#################

		#upperLeft
		upLeFroX = -(b / 2)
		upLeFroY = a
		upLeFroZ = b / 2
		upperLeftFro = [upLeFroX, upLeFroY, upLeFroZ]

		#upperRight
		upRiFroX = b / 2
		upRiFroY = a
		upRiFroZ = b / 2
		upperRightFro = [upRiFroX, upRiFroY, upRiFroZ]

		#lowerLeft
		loLeFroX = -(b / 2)
		loLeFroY = 0.0
		loLeFroZ = b / 2
		lowerLeftFro = [loLeFroX, loLeFroY, loLeFroZ]

		#lowerRight
		loRiFroX = b / 2
		loRiFroY = 0.0
		loRiFroZ = b / 2
		lowerRightFro = [loRiFroX, loRiFroY, loRiFroZ]

		################
		####LeftWall####
		################

		#upperLeft
		upLeLefX = -(b / 2)
		upLeLefY = a
		upLeLefZ = -(b / 2)
		upperLeftLef = [upLeLefX, upLeLefY, upLeLefZ]

		#upperRight
		upRiLefX = -(b / 2)
		upRiLefY = a
		upRiLefZ = b / 2
		upperRightLef = [upRiLefX, upRiLefY, upRiLefZ]

		#lowerLeft
		loLeLefX = -(b / 2)
		loLeLefY = 0.0
		loLeLefZ = -(b / 2)
		lowerLeftLef = [loLeLefX, loLeLefY, loLeLefZ]

		#lowerRight
		loRiLefX = -(b / 2)
		loRiLefY = 0.0
		loRiLefZ = b / 2
		lowerRightLef = [loRiLefX, loRiLefY, loRiLefZ]

		##################
		####BottomWall####
		##################

		#upperLeft
		upLeBotX = -(b / 2)
		upLeBotY = 0.0
		upLeBotZ = b / 2
		upperLeftBot = [upLeBotX, upLeBotY, upLeBotZ]

		#upperRight
		upRiBotX = b / 2
		upRiBotY = 0.0
		upRiBotZ = b / 2
		upperRightBot = [upRiBotX, upRiBotY, upRiBotZ]

		#lowerLeft
		loLeBotX = -(b / 2)
		loLeBotY = 0.0
		loLeBotZ = a
		lowerLeftBot = [loLeBotX, loLeBotY, loLeBotZ]

		#lowerRight
		loRiBotX = b / 2
		loRiBotY = 0.0
		loRiBotZ = a
		lowerRightBot = [loRiBotX, loRiBotY, loRiBotZ]

		#################
		####RightWall####
		#################

		#upperLeft
		upLeRigX = b / 2
		upLeRigY = a
		upLeRigZ = b / 2
		upperLeftRig = [upLeRigX, upLeRigY, upLeRigZ]

		#upperRight
		upRiRigX = b / 2
		upRiRigY = a
		upRiRigZ = -(b / 2)
		upperRightRig = [upRiRigX, upRiRigY, upRiRigZ]

		#lowerLeft
		loLeRigX = b / 2
		loLeRigY = 0.0
		loLeRigZ = b / 2
		lowerLeftRig = [loLeRigX, loLeRigY, loLeRigZ]

		#lowerRight
		loRiRigX = b / 2
		loRiRigY = 0.0
		loRiRigZ = -(b / 2)
		lowerRightRig = [loRiRigX, loRiRigY, loRiRigZ]

	else:
		#################
		####FrontWall####
		#################

		#upperLeft
		upLeFroX = -(b / 2)
		upLeFroY = a
		upLeFroZ = c
		upperLeftFro = [upLeFroX, upLeFroY, upLeFroZ]

		#upperRight
		upRiFroX = b / 2
		upRiFroY = a
		upRiFroZ = c
		upperRightFro = [upRiFroX, upRiFroY, upRiFroZ]

		#lowerLeft
		loLeFroX = -(b / 2)
		loLeFroY = 0.0
		loLeFroZ = c
		lowerLeftFro = [loLeFroX, loLeFroY, loLeFroZ]

		#lowerRight
		loRiFroX = b / 2
		loRiFroY = 0.0
		loRiFroZ = c
		lowerRightFro = [loRiFroX, loRiFroY, loRiFroZ]

		################
		####LeftWall####
		################

		#upperLeft
		upLeLefX = -(b / 2)
		upLeLefY = a
		upLeLefZ = -(b - c)
		upperLeftLef = [upLeLefX, upLeLefY, upLeLefZ]

		#upperRight
		upRiLefX = -(b / 2)
		upRiLefY = a
		upRiLefZ = c
		upperRightLef = [upRiLefX, upRiLefY, upRiLefZ]

		#lowerLeft
		loLeLefX = -(b / 2)
		loLeLefY = 0.0
		loLeLefZ = -(b - c)
		lowerLeftLef = [loLeLefX, loLeLefY, loLeLefZ]

		#lowerRight
		loRiLefX = -(b / 2)
		loRiLefY = 0.0
		loRiLefZ = c
		lowerRightLef = [loRiLefX, loRiLefY, loRiLefZ]

		##################
		####BottomWall####
		##################

		#upperLeft
		upLeBotX = -(b / 2)
		upLeBotY = 0.0
		upLeBotZ = c
		upperLeftBot = [upLeBotX, upLeBotY, upLeBotZ]

		#upperRight
		upRiBotX = b / 2
		upRiBotY = 0.0
		upRiBotZ = c
		upperRightBot = [upRiBotX, upRiBotY, upRiBotZ]

		#lowerLeft
		loLeBotX = -(b / 2)
		loLeBotY = 0.0
		loLeBotZ = a
		lowerLeftBot = [loLeBotX, loLeBotY, loLeBotZ]

		#lowerRight
		loRiBotX = b / 2
		loRiBotY = 0.0
		loRiBotZ = a
		lowerRightBot = [loRiBotX, loRiBotY, loRiBotZ]

		#################
		####RightWall####
		#################
		
		#upperLeft
		upLeRigX = b / 2
		upLeRigY = a
		upLeRigZ = c
		upperLeftRig = [upLeRigX, upLeRigY, upLeRigZ]

		#upperRight
		upRiRigX = b / 2
		upRiRigY = a
		upRiRigZ = -(b -c)
		upperRightRig = [upRiRigX, upRiRigY, upRiRigZ]

		#lowerLeft
		loLeRigX = b / 2
		loLeRigY = 0.0
		loLeRigZ = c
		lowerLeftRig = [loLeRigX, loLeRigY, loLeRigZ]

		#lowerRight
		loRiRigX = b / 2
		loRiRigY = 0.0
		loRiRigZ = -(b - c)
		lowerRightRig = [loRiRigX, loRiRigY, loRiRigZ]


	saveName = vizinput.input("Name the file:\n(leave blank for default)")

	if saveName == "":
		saveName = "cave_settings"

	textFile = open("./" + saveName + ".txt","w")
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
	
	answerCave2 = vizinput.ask("Do you want to get a graphical representation?")

	if answerCave2 == 1:
		viz.setMultiSample(4)
		viz.fov(70)
		viz.go()

		viz.mouse.setOverride(viz.ON)

		viz.MainView.setPosition([0,20,-20])
		viz.MainView.setEuler([0,35,0])

		pic = viz.addTexture("./walltexture.png")

		wallFront = vizshape.addPlane(size = (19.2, 12))
		wallFront.setPosition([0,6,9.6])
		wallFront.setEuler([0,-90,0])
		wallFront.texture(pic)

		wallLeft = vizshape.addPlane(size = (19.2, 12))
		wallLeft.setPosition([-9.6,6,0])
		wallLeft.setEuler([90,90,0])
		wallLeft.texture(pic)

		wallRigth = vizshape.addPlane(size = (19.2, 12))
		wallRigth.setPosition([9.6,6,0])
		wallRigth.setEuler([90,-90,0])
		wallRigth.texture(pic)

		wallBottom = vizshape.addPlane(size = (19.2, 12))
		wallBottom.setPosition([0,0,3.6])
		wallBottom.texture(pic)

		pointA = vizshape.addSphere(color = viz.BLUE)
		pointA.setScale(.5,.5,.5)
		pointA.setPosition([-9.6,0,9.6])
		pointB = vizshape.addSphere(color = viz.RED)
		pointB.setScale(.5,.5,.5)
		pointB.setPosition([9.6,0,9.6])
		pointC = vizshape.addSphere(color = viz.GREEN)
		pointC.setScale(.5,.5,.5)
		pointC.setPosition([-9.6,0,-9.6])
		pointD = vizshape.addSphere(color = viz.YELLOW)
		pointD.setScale(.5,.5,.5)
		pointD.setPosition([9.6,0,-9.6])
		pointE = vizshape.addSphere(color = viz.ORANGE_RED)
		pointE.setScale(.5,.5,.5)
		pointE.setPosition([-9.6,12,9.6])
		pointF = vizshape.addSphere(color = viz.PURPLE)
		pointF.setScale(.5,.5,.5)
		pointF.setPosition([9.6,12,9.6])
		pointG = vizshape.addSphere(color = viz.ROSE)
		pointG.setScale(.5,.5,.5)
		pointG.setPosition([-9.6,12,-9.6])
		pointH = vizshape.addSphere(color = viz.AZURE)
		pointH.setScale(.5,.5,.5)
		pointH.setPosition([9.6,12,-9.6])
		pointI = vizshape.addSphere(color = viz.BLACK)
		pointI.setScale(.5,.5,.5)
		pointI.setPosition([0,0,0])

		textA = viz.addText(str(lowerLeftFro), pos = [-9.5,.5,9.6], align = viz.ALIGN_LEFT_BOTTOM, color = viz.BLACK)
		textB = viz.addText(str(lowerRightFro), pos = [9.5,.5,9.6], align = viz.ALIGN_RIGHT_BOTTOM, color = viz.BLACK)
		textC = viz.addText(str(lowerLeftLef), pos = [-9.6,.5,-9.6], align = viz.ALIGN_LEFT_BOTTOM)
		textD = viz.addText(str(lowerRightRig), pos = [9.6,.5,-9.6], align = viz.ALIGN_RIGHT_BOTTOM)
		textE = viz.addText(str(upperLeftFro), pos = [-9.6,12.5,9.6], align = viz.ALIGN_LEFT_BOTTOM)
		textF = viz.addText(str(upperRightFro), pos = [9.6,12.5,9.6], align = viz.ALIGN_RIGHT_BOTTOM)
		textG = viz.addText(str(upperLeftLef), pos = [-10.4,12.5,-9.6], align = viz.ALIGN_LEFT_BOTTOM)
		textH = viz.addText(str(upperRightRig), pos = [10,12.5,-9.6], align = viz.ALIGN_RIGHT_BOTTOM)
		textI = viz.addText(str(centerPoint), pos = [0,.5,0], align = viz.ALIGN_CENTER_BOTTOM)

##################
####Power-Wall####
##################
		
elif choice == 1:
	loop = True
	while loop == True:
		wallHeight2 = vizinput.input("Enter the wall height:")
		wallWidth2 = vizinput.input("Enter the wall width:")
		offsetInput = vizinput.input("Enter the distance between floor and lower display edge:")
		
		if wallHeight2 == "" or wallWidth2 == "" or offsetInput == "":
			vizinput.message("Error, there was no data recorded. Please enter a value.")
			loop = True
			
		else:
			loop = False
	
	answerPoWa1 = vizinput.ask("The recommended tracker origin is 1 meters from the wall.\nDo you want to keep it?")
	
	if answerPoWa1 == 1:
		f = 1.0
		trackerOrigin = [0.0,1.0,0.0]
		
		d = float(wallHeight2)
		e = float(wallWidth2)
		
	else:
		loop = True
		while loop == True:
			centerInput2 = vizinput.input("Enter the distance between wall and tracker origin:")
			
			if centerInput2 == "":
				vizinput.message("Error, there was no data recorded. Please enter a value.")
				loop = True
			else:
				loop = False

		d = float(wallHeight2)
		e = float(wallWidth2)
		f = float(centerInput2)
		
	h = float(offsetInput)
		
	V = round(math.sqrt((d*d) / 2))
	
	#upperLeft
	upLePowX = -(e / 2)
	upLePowY = V + h
	upLePowZ = V + f
	upperLeftPow = [upLePowX, upLePowY, upLePowZ]
	
	#upperRight
	upRiPowX = e / 2
	upRiPowY = V + h
	upRiPowZ = V + f
	upperRightPow = [upRiPowX, upRiPowY, upRiPowZ]	
	
	#lowerLeft
	loLePowX = -(e / 2)
	loLePowY = h
	loLePowZ = f
	lowerLeftPow = [loLePowX, loLePowY, loLePowZ]
	
	#lowerRight
	loRiPowX = e / 2
	loRiPowY = h
	loRiPowZ = f
	lowerRightPow = [loRiPowX, loRiPowY, loRiPowZ]
	
	saveName2 = vizinput.input("Name the file:\n(leave blank for default)")

	if saveName2 == "":
		saveName2 = "powerwall_settings"
		
	textFile2 = open("./" + saveName2 + ".txt","w")
	textFile2.write("The following shows the coordinats for a powerwall 45 degrees tilted.\n\n")
	textFile2.write("Upper left corner: "+str(upperLeftPow)+"\nUpper right corner: "+str(upperRightPow))
	textFile2.write("\nLower left corner: "+str(lowerLeftPow)+"\nUpper right corner: "+str(lowerRightPow))
	textFile2.write("\n\n\nNote:\nThis shows only the coordinats and can not be used as a configuration file.")

	answerPoWa2 = vizinput.ask("Do you want to get a graphical representation?")

	if answerPoWa2 == 1:
		viz.setMultiSample(4)
		viz.fov(70)
		viz.go()

		viz.mouse.setOverride(viz.ON)

		viz.MainView.setPosition([0,0,-30])

		pic = viz.addTexture("./walltexture.png")

		wallPower = vizshape.addPlane(size = (38.4, 24))
		wallPower.setPosition([0,0,0])
		wallPower.setEuler([0,-90,0])
		wallPower.texture(pic)

		pointA = vizshape.addSphere(color = viz.BLUE)
		pointA.setScale(.5,.5,.5)
		pointA.setPosition([-19.2,12,0])
		pointB = vizshape.addSphere(color = viz.RED)
		pointB.setScale(.5,.5,.5)
		pointB.setPosition([19.2,12,0])
		pointC = vizshape.addSphere(color = viz.GREEN)
		pointC.setScale(.5,.5,.5)
		pointC.setPosition([-19.2,-12,0])
		pointD = vizshape.addSphere(color = viz.YELLOW)
		pointD.setScale(.5,.5,.5)
		pointD.setPosition([19.2,-12,0])

		textA = viz.addText(str(upperLeftPow), pos = [-19.5,12.5,0], align = viz.ALIGN_LEFT_BOTTOM)
		textB = viz.addText(str(upperRightPow), pos = [19.5,12.5,0], align = viz.ALIGN_RIGHT_BOTTOM)
		textC = viz.addText(str(lowerLeftPow), pos = [-19.6,-12.5,0], align = viz.ALIGN_LEFT_TOP)
		textD = viz.addText(str(lowerRightPow), pos = [19.6,-12.5,0], align = viz.ALIGN_RIGHT_TOP)