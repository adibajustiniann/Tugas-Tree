# Nama		: Adiba Justinian 	
# NIM		: 24060120130080	
# Tanggal	: 5 Desember 2020	
# Deskripsi	: Tugas Tree	

from Code import*

#1
#fungsi RepPostfix
#def spek
#RepPostfix : pohon biner --> list of element
#RepPostfix (P) memberikan representasi linier (dalam bentuk list)
#dengan urutan elemen list sesuai dengan urutan penulisan pohon secara postfix
#/L R A\
def RepPostfix(P):
	if IsOneElmtPB(P):
		return [Akar(P)]
	else:
		if IsBiner(P):
			return RepPostfix(Left(P)) + RepPostfix(Right(P)) + [Akar(P)]
		elif IsUnerLeft(P):
			return RepPostfix(Left(P)) + [Akar(P)]
		elif IsUnerRight(P):
			return RepPostfix(Right(P)) + [Akar(P)]

#2
#fungsi RepInfix
#def spek
#RepInfix : pohon biner --> list of element
#RepInfix (P) memberikan representasi linier (dalam bentuk list)
#dengan urutan elemen list sesuai dengan urutan penulisan pohon secara infix
#/L A R\
def RepInfix(P):
	if IsOneElmtPB(P):
		return [Akar(P)]
	else:
		if IsBiner(P):
			return RepInfix(Left(P)) + [Akar(P)] + RepInfix(Right(P))
		elif IsUnerLeft(P):
			return RepInfix(Left(P)) + [Akar(P)]
		elif IsUnerRight(P):
			return [Akar(P)] + RepInfix(Right(P))

#3
#fungsi Tinggi
#def spek
#Tinggi : pohon biner --> integer
#Tinggi (P) memberikan banyaknya level dari pohon biner
#akar merupakan level 0
def TinggiKiri(P):
	if IsOneElmtPB(P):
		return 0
	else:
		if IsBiner(P):
			return 1 + TinggiKiri(Left(P))
		elif IsUnerLeft(P):
			return 1 + TinggiKiri(Left(P))
		elif IsUnerRight(P):
			return 1 + TinggiKiri(Right(P))
		else:
			return 0

def TinggiKanan(P):
	if IsOneElmtPB(P):
		return 0
	else:
		if IsBiner(P):
			return 1 + TinggiKanan(Right(P)) 
		elif IsUnerLeft(P):
			return 1 + TinggiKanan(Left(P))
		elif IsUnerRight(P):
			return 1 + TinggiKanan(Right(P))
		else:
			return 0

def Tinggi(P):
	if TinggiKanan(P) > TinggiKiri(P):
		return TinggiKanan(P)
	else:
		return TinggiKiri(P)

#4
#fungsi SumLRDaun
#def spek
#SumLRDaun : pohon biner --> integer
#SumLRDaun (P) menjumlahkan daun paling kiri dan daun paling kanan
def LeftDaun(P):
	if IsOneElmtPB(P):
		return Akar(P)
	else:
		if IsBiner(P): 
			return LeftDaun(Left(P))
		elif IsUnerLeft(P):
			return LeftDaun(Left(P))
		elif IsUnerRight(P):
			return None

def RightDaun(P):
	if IsOneElmtPB(P):
		return Akar(P)
	else:
		if IsBiner(P): 
			return RightDaun(Right(P))
		elif IsUnerLeft(P):
			return None
		elif IsUnerRight(P):
			return RightDaun(Right(P))

def SumLRDaun(P):
	if IsTreeEmpty(P):
		return None
	else:
		return LeftDaun(P) + RightDaun(P)

#5		
#fungsi IsMember
#def spek
#IsMember : pohon biner --> boolean
#IsMember (P,x) menentukan apakah elemen x merupakan
#anggota dari pohon biner bersangkutan
def IsMember(P,x):
	if IsTreeEmpty(P):
		return False
	else:
		if Akar(P) == x:
			return True
		else:
			return IsMember(Left(P),x) or IsMember(Right(P),x)

#Aplikasi
print ('===RepPostfix===')
print (RepPostfix(P0))
print (RepPostfix(P1))
print (RepPostfix(P2))
print ('===RepInfix===')
print (RepInfix(P0))
print (RepInfix(P1))
print (RepInfix(P2))
print ('===Tinggi===')
print (Tinggi(P0))
print (Tinggi(P1))
print (Tinggi(P2))
print ('===SumLRDaun===')
print (SumLRDaun(P0))
print (SumLRDaun(P1))
print (SumLRDaun(P2))
print ('===IsMember===')
print (IsMember(P0,1))
print (IsMember(P1,3))
print (IsMember(P2,'a'))
print (IsMember(P2,'r'))