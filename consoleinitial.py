class NumbersRoman:

	def __init__(self, arg):
		super(NumbersRoman, self).__init__()
		self.arg = arg
	def ValidateNumber(entervalue):
		letters=['I','V','X','L','C','D','M']
		retvalue=True
		for x in list(entervalue):
			if (x not in letters):
				retvalue=False
				break

		return retvalue
	def RomToDec(entervalue):
		sumvalue=0
		itembefore=""
		numberbefore=0
		if not NumbersRoman.ValidateNumber(entervalue):
			return "NAN"

		for item in range(len(entervalue)):
			strnumber=entervalue[item]
			returnvalue=NumbersRoman.LetterToDecimal(strnumber)
			#print(item,strnumber,returnvalue)
			if numberbefore < returnvalue:
				returnvalue-=(numberbefore *2)
			numberbefore=returnvalue	
			sumvalue += returnvalue
		return sumvalue
				
	def LetterToDecimal(param):
		if param == "I":
			return 1
		elif param == "V":
			return 5
		elif param == "X":
			return 10
		elif param == "L":
			return 50	
		elif param == "C":
			return 100
		elif param == "D":
			return 500
		elif param == "M":
			return 1000													
		else:
			return 0
		
	def converttoroman(valor):
		strreturn=""
		letter=""
		if not (str(valor).isdigit()):
			return "NAN"
		if valor == 0:
			return ""	
		else:
			if NumbersRoman.isFourOrNine(valor):
				letter = NumbersRoman.FourOrNine(valor)
				decrease =NumbersRoman.DecreaseFourOrNine(valor)
			else:
				letter=NumbersRoman.Letter(valor)
				decrease=NumbersRoman.Decrease(valor)
			strreturn = strreturn + letter + NumbersRoman.converttoroman(valor-decrease)

		return strreturn

	def DecreaseFourOrNine(valor):
		repeatnumber=len(str(valor))-1
		digitnumber=int(str(valor)[0])
		strbeforenumber=str(digitnumber)
		for valor in range(repeatnumber):
			strbeforenumber += "0"

		return int(strbeforenumber)

	def FourOrNine(valor):
		repeatnumber=len(str(valor))-1
		digitnumber=int(str(valor)[0])
		strbeforenumber="1"
		strafternumber=str(digitnumber + 1)
		for valor in range(repeatnumber):
			strbeforenumber += "0"
		for valor in range(repeatnumber):
			strafternumber += "0"
		antes=NumbersRoman.Letter(int(strbeforenumber))
		despues=NumbersRoman.Letter(int(strafternumber))
		return antes + despues
	def isFourOrNine(valor):
		strvalor=str(valor)
		numbers=len(strvalor)
		numfirstdigit=0
		if numbers <= 0:
			return	False	
		else:
			numfirstdigit=int(strvalor[0])
		if numfirstdigit == 4 or numfirstdigit == 9:
			return True
		else:
			return False

	def Letter(valor):
		strLetter=""
		if valor >= 1 and valor < 4:
			strLetter="I"
		elif valor >=4 and valor <9:
			strLetter = "V"
		elif valor >=9 and valor <50:
			strLetter="X"
		elif valor >=50 and valor < 90:
			strLetter="L"
		elif valor >=90 and valor < 100:
			strLetter="X"		
		elif valor >=100 and valor < 500:
			strLetter="C"
		elif valor >=500 and valor < 1000:
			strLetter="D"	
		elif valor >=1000 and valor < 5000:
			strLetter="M"			
		return strLetter

	def Decrease(valor):
		decrease=0
		if valor >= 1 and valor < 4:
			decrease=1
		elif valor >=4 and valor <9:
			decrease = 5
		elif valor >=9 and valor <50:
			decrease=10
		elif valor >=50 and valor < 90:
			decrease=50
		elif valor >=90 and valor < 100:
			decrease=90			
		elif valor >=100 and valor < 500:
			decrease=100
		elif valor >=500 and valor < 1000:
			decrease=500	
		elif valor >=1000 and valor < 5000:
			decrease=1000			
		return decrease

		
		