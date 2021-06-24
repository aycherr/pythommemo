import math

print("****** Method Kern ********")

#lES CONSTANTS
#Les Constants de cote chaud

Tce = float(71)
Tcs = float(49)
mc=float()
cpc=float(2.38)
kc = float(0.129)
viscoc = float(0.0002)
Rdc = float(0.000025)
Sgc = float(0.685)
mvc = float(685)

#Les Constants de cote froid
Tfe = float(24)
Tfs = float(49)
mf= float(67500)
cpf=float(2)
kf = float(0.143)
Rdf = float(0.000049)
Sgf = float(0.8)
visco = float(input(0.0016))
mv = float(input(800))

#constants general
R = float(0.88)
P = float(0.529)
A = float()
do=float()
Lt = float()
np = float()
di=float()
visco=float()
Re = float()



#=======================================================================================================================================================
#energy balance
Q = mf*cpf*(Tfs-Tfe)
mc= Q/(cpc*(Tce-Tcs))
print("La puissance = ",Q)
print("Le debit de fluid chaud = ",mc)


#factor de correction
S1 = math.sqrt((math.pow(R,2) + 1 ))* math.log((1-P)/(1-R*P))
S2 = (R-1)*math.log((2-P*(R+1-(math.sqrt(math.pow(R,2)+1))))/(2-P*(R+1+math.sqrt(math.pow(R,2)+1))))
Ft = S1/S2
print("le facteur de correction = ",Ft)

#DTLM
DTa=Tce-Tfs                                                                                                 
DTb=Tcs-Tfe
DTLM =(DTa-DTb)/(math.log(DTa/DTb))
print("DTLM = ",DTLM)

#la surface d'echange 
print("Enter le coef d'echange assume :")
Uass = float(input()) #variable
A = ((Q/3600)/(Uass*Ft*DTLM))*(10**3)
print("la surface d'echange = ",A)

#le nombre des tubes 
print("do :")
do = float(input())   #variable
print("La Longueur :")
Lt = float(input())    #variable
nt = (A) /(3.14*do*10**(-3)*Lt)
print("nombre du tubes",nt)

#la vitesse de fluide
print("le nombre des passes :")
np = float(input())  #variable

print("le diametre interieur :")
di = float(input())    #variable

print("le nombre des tubes assume :")
nta = float(input())    #variable

Re = (4*(mf/3600)*(np/nta))/(3.14*di*10**(-3)*visco)
print("le nombre de RYNOLDS cote tubes = ",Re)
V=(Re*visco)/(di*10**(-3)*mv)
print("La vitesse de fluide cote tubes = ",V)

#le coef d'echange cote tubes
print("le coeficient convectif:")
jH = float(input())    #variable

cpt = cpf
kt = kf
viscot = visco

pr3 = ((viscot*cpt*10**3)/kt)**(0.3333333)
h = (kt*jH*(pr3))/(di*10**(-3))
print("pr=",pr3)
print("le coeficient d'echange cote tubes h=",h)


#le diametre interieur de calandre
print("'square' or 'triangle' pitch ?")
st = str(input())
ys = "S"
nn = "T"
print("le pitch = ")
Pt = float(input())
if (st==ys) :
    De= (4*((Pt**2)-(((3.14)*(do**2))/4)))/(3.14*do)
    print("De = ",De)

elif (st==nn):
    De = (4*((0.5*Pt*0.86*Pt)-(0.5*(3.14*do**2)/4)))/(0.5*3.14*do)
    print("De = ",De)


#le coefcient d'echange cote calandre
print("enter clearence = ")
clr = float(input())   #variable

print("enter baffle spacing = ")
spacing = float(input())    #variable

print("le diametre exterieur de la calandre = ")
Ds = float(input())    #variable

a=((clr*10**(-3))*(spacing*10**(-3))*(Ds*10**(-3)))/(Pt*10**(-3))
print("shell side cross flow area = ",a)

Gs = (mc/3600)/a
print("Gs = ",Gs)

Vc = Gs/mvc
print("la vitesse de fluide cote calandre = ",Vc)

Re2 = (De*10**(-3)*Gs)/viscoc
print("Re cote calansre = ",Re2)



cpt = cpc
kt = kc
viscot = viscoc


print("enter jH = ")
jH2 = float(input())   #variable
jH=jH2
pr3 = ((viscot*cpt*10**3)/kt)**(0.3333333)
h2 = (kt*jH*(pr3))/(De*10**(-3))

print("coef d'echange cote calandre :",h2)

#le coeficient d'echange globale

print(" Conductivite de materiaux de tube = ")
km = float(input())     #variable
A0 = float(3.14 *(do**2))
Ai = float(3.14 *(di**2))

Ucal = 1/((1/h2)+(Rdc)+(A0/Ai)*((do-di)*10**(-3))/((2*km))+((A0/Ai)*(1/h))+((A0/Ai)*Rdf))

print("Ucal = ",Ucal)
print("Uass",Uass)

#error
error = (Ucal - Uass)/(Uass)
print("******* error = ",error ,"********")

#les petes de charges 
print("\n \n \n *********  LES PERTES DE CHARGES  ***********")

print(" facteur de friction f = ")
f = float(input())             #variable

DPt = np*(((8*f)*(Lt/(di*10**(-3))))+2.5)*((mv*(V**2))/2)
print("Les pertes de charges cote tube DPt = ", DPt*10**(-5))

#les pertes de charges cote calandre

print(" facteur de friction cote calandre f = ")
fs = float(input())      #variable
DPs = 8*(fs)*(Ds/De)*(Lt/spacing*10**(-3))*(((mvc*Vc**2))/2)
print("les pertes de charges cote calandre = ",DPs)

#Over Surface
hio = h*(di/do)
print("hio = ",hio)
Uc = (h2*hio)/(h2+hio)
print("Uc = ", Uc)
osc = (Uc - Ucal)/Uc
print("over surface osc = ",osc)

#over design
Asup = 3.14*do*10**(-3)*Lt*nta
ovd = (Asup - A)/A
print("Over design ovd = ",ovd)









input()



