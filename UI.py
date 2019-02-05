try:
    from tkinter import *
except:
    from Tkinter import *
from tkinter import font
import time
import threading

root = Tk()

root.geometry("800x400")  #Taille Fenêtre
root.configure(background="#404040") #Couleur fond d'écran

##########  TOUTES LES IMAGES  ##########################################################################################################################################################

                                   #Noms des boutons

ac = PhotoImage(file="image/ac.png") #Accueil
iea = PhotoImage(file="image/iea.png") #Fond d'écran accueil

pa = PhotoImage(file="image/pa.png") #Programme d'arrosage
am = PhotoImage(file="image/am.png") #Arrosage manuel
ap = PhotoImage(file="image/ap.png") #Arrosage programmé
ah = PhotoImage(file="image/ah.png") #Arrosage humidité

m = PhotoImage(file="image/m.png") #Météo
th = PhotoImage(file="image/th.png") #Taux d'humidité

re = PhotoImage(file="image/re.png") #Réglages
sa = PhotoImage(file="image/sa.png") #Activer sécheresse
sd = PhotoImage(file="image/sd.png") #désctiver sécheresse
dz = PhotoImage(file="image/dz.png") #Descrption des zones

da = PhotoImage(file="image/da.png") #Date
he = PhotoImage(file="image/he.png") #Heure

r = PhotoImage(file="image/r.png") #Retour
v = PhotoImage(file="image/v.png") #Valider
vActif = PhotoImage(file="image/vActif.png") #Valider en vert
acti = PhotoImage(file="image/acti.png") #Activer
dacti = PhotoImage(file="image/dacti.png") #Désactiver

cz = PhotoImage(file="image/cz.png") #Choix des zones
du = PhotoImage(file="image/du.png") #Durée
h = PhotoImage(file="image/h.png") #Horaire

act = PhotoImage(file="image/act.png") #Actualiser
ve = PhotoImage(file="image/ve.png") #Veille

bgVeille = PhotoImage(file="image/bgVeille.png") #Fond d'écran veille

h0p0 = PhotoImage(file="image/programmeEnCours/h0p0.png") 
h0p1 = PhotoImage(file="image/programmeEnCours/h0p1.png") 
h1p0 = PhotoImage(file="image/programmeEnCours/h1p0.png") 
h1p1 = PhotoImage(file="image/programmeEnCours/h1p1.png") 

sIcone = PhotoImage(file="image/secheresseIcone.png")

                                   #Images
ipecAccueil = PhotoImage(file="image/pageEnCours/pecAccueil.png") #Ipec Accueil
ipecMeteo = PhotoImage(file="image/pageEnCours/pecMeteo.png") #Ipec Météo
ipecTauxHumidite = PhotoImage(file="image/pageEnCours/pecTauxHumidite.png") #Ipec Taux d'humidité

ipecProgrammeArrosage = PhotoImage(file="image/pageEnCours/programmeArrosage/pecProgrammeArrosage.png") #Ipec Programme d'arrosage
ipecManuel = PhotoImage(file="image/pageEnCours/programmeArrosage/pecManuel.png") #Ipec Arrosage Manuel
ipecProgramme = PhotoImage(file="image/pageEnCours/programmeArrosage/pecProgramme.png") #Ipec Arrosage Programme
ipecHumidite = PhotoImage(file="image/pageEnCours/programmeArrosage/pecHumidite.png") #Ipec Arrosage Humidité
ipecProgrammeArrosage = PhotoImage(file="image/pageEnCours/programmeArrosage/pecProgrammeArrosage.png") #Ipec Programme d'arrosage

ipecReglages = PhotoImage(file="image/pageEnCours/reglages/pecReglages.png") #Ipec Réglages
ipecDZones = PhotoImage(file="image/pageEnCours/reglages/pecDZones.png") #Ipec Nom des zones

                                    #Zones
iZ1 = PhotoImage(file="image/zones/zone1.png")
iZ2 = PhotoImage(file="image/zones/zone2.png")
iZ3 = PhotoImage(file="image/zones/zone3.png")
iZ4 = PhotoImage(file="image/zones/zone4.png")
iZ5 = PhotoImage(file="image/zones/zone5.png")

                                    #Durée
xMinutes = PhotoImage(file="image/Horaire Durée/xMinutes.png")
flecheHaut = PhotoImage(file="image/Horaire Durée/flecheHaut.png")
p10Haut = PhotoImage(file="image/Horaire Durée/+10Haut.png")
flecheBas = PhotoImage(file="image/Horaire Durée/flecheBas.png")
p10Bas = PhotoImage(file="image/Horaire Durée/+10Bas.png")

                                    #Horaire
selectHeure = PhotoImage(file="image/Horaire Durée/selectHeure.png")
selectMinutes = PhotoImage(file="image/Horaire Durée/selectMinutes.png")
xHoraire = PhotoImage(file="image/Horaire Durée/xHoraire.png")

                                    #Taux d'humidité
TH1 = PhotoImage(file="image/TH/TH1.png")
TH2 = PhotoImage(file="image/TH/TH2.png")
TH3 = PhotoImage(file="image/TH/TH3.png")
TH4 = PhotoImage(file="image/TH/TH4.png")
TH5 = PhotoImage(file="image/TH/TH5.png")
TH25 = PhotoImage(file="image/TH/TH25.png")
TH50 = PhotoImage(file="image/TH/TH50.png")
TH75 = PhotoImage(file="image/TH/TH75.png")
TH100 = PhotoImage(file="image/TH/TH100.png")

                                    #Meteo
mHeure = PhotoImage(file="image/meteo/mHeure.png")
mTemperature = PhotoImage(file="image/meteo/mTemperature.png")
mTMax = PhotoImage(file="image/meteo/mTMax.png")
mTMin = PhotoImage(file="image/meteo/mTMin.png")
                                    #Symboles météo
sun = PhotoImage(file="image/meteo/symboles/sun.png")
sunCloud = PhotoImage(file="image/meteo/symboles/sunCloud.png")
cloud = PhotoImage(file="image/meteo/symboles/cloud.png")
rain = PhotoImage(file="image/meteo/symboles/rain.png")
snow = PhotoImage(file="image/meteo/symboles/snow.png")
storm = PhotoImage(file="image/meteo/symboles/storm.png")
                        
                                    #Réglages desc Zones
warnClavier = PhotoImage(file="image/descZones/warnClavier.png")
iDZ = PhotoImage(file="image/descZones/iDZ.png")
edit = PhotoImage(file="image/descZones/edit.png")
ok = PhotoImage(file="image/descZones/ok.png")

                                    #imagesCentrales
imageAide = PhotoImage(file="image/imagesCentrales/imageAide.png")
imageHumidite = PhotoImage(file="image/imagesCentrales/imageHumidite.png")
imageManuel = PhotoImage(file="image/imagesCentrales/imageManuel.png")
imageProgramme = PhotoImage(file="image/imagesCentrales/imageProgramme.png")
mpm = PhotoImage(file="image/imagesCentrales/mpm.png")
selectZoneSVP = PhotoImage(file="image/imagesCentrales/selectZoneSVP.png")
imageReglages = PhotoImage(file="image/imagesCentrales/imageReglages.png")

#######  POLICES  ##################################################################################################################################################################

policeNombreDurée=font.Font(family='Helvetica', size=20)
policeHH=font.Font(family='Helvetica', size=20, underline = False)
policeHM=font.Font(family='Helvetica', size=20, underline = False)
policeTH=font.Font(family='Arial', size=16, weight="bold")
policeM1=font.Font(family='Arial', size=25)
policeM2=font.Font(family='Arial', size=16)
policeDZ=font.Font(family='Helvetica', size=18)

#######  VARIABLES  ##################################################################################################################################################################

arrosageManuelActif=0 # =1 si arrosage manuel actif
arrosageProgrammeActif=0 # =1 si arrosage programme actif
sArrosageProgrammeActif=0 # (Initialisation) Stocke la valeur de "arrosageProgrammeActif" pendant secheresse
arrosageHumiditeActif=0 # (Initialisation) Utilisé dans "Arrosage humidité"
sArrosageHumiditeActif=0  # (Initialisation) Stocke la valeur de "ArrosageHumiditéActif" pendant secheresse
secheresseActif=0 # (Initialisation) =1 si secheresse actif
acceuilActif=1 # (Initialisation) =1 si accueil actif
sdu=0 # secheresse deja utilisé 
#Zones selectionées en mode manuel
#mZ1=0 ,mZ2=0 ,mZ3=0 ,mZ4=0 ,mZ5=0
#récupérées depuis vArrosageManuel

#---------------------------------

#Couleur des boutons de choix de zones en mode manuel
def couleurBoutonZonesManuel():
    global cadMZ1, cadMZ2, cadMZ3, cadMZ4, cadMZ5
    if mZ1==0:
        cadMZ1="red" #Bouton zone 1 rouge
    else:
        cadMZ1="green" #Bouton zone 1 vert
    if mZ2==0:
        cadMZ2="red" #Bouton zone 2 rouge
    else:
        cadMZ2="green" #Bouton zone 2 vert
    if mZ3==0:
        cadMZ3="red" #Bouton zone 3 rouge
    else:
        cadMZ3="green" #Bouton zone 3 vert
    if mZ4==0:
        cadMZ4="red" #Bouton zone 4 rouge
    else:
        cadMZ4="green" #Bouton zone 4 vert
    if mZ5==0:
        cadMZ5="red" #Bouton zone 5 rouge
    else:
        cadMZ5="green" #Bouton zone 5 vert

#----------------------------------

#Zones selectionées en mode programmé

pZ1=0
pZ2=0
pZ3=0
pZ4=0
pZ5=0

#----------------------------------

#Couleur des boutons de choix de zones en mode Programmé
def couleurBoutonZonesProgramme():
    global cadPZ1, cadPZ2, cadPZ3, cadPZ4, cadPZ5
    if pZ1==0:
        cadPZ1="red" #Bouton zone 1 rouge
    else:
        cadPZ1="green" #Bouton zone 1 vert
    if pZ2==0:
        cadPZ2="red" #Bouton zone 2 rouge
    else:
        cadPZ2="green" #Bouton zone 2 vert
    if pZ3==0:
        cadPZ3="red" #Bouton zone 3 rouge
    else:
        cadPZ3="green" #Bouton zone 3 vert
    if pZ4==0:
        cadPZ4="red" #Bouton zone 4 rouge
    else:
        cadPZ4="green" #Bouton zone 4 vert
    if pZ5==0:
        cadPZ5="red" #Bouton zone 5 rouge
    else:
        cadPZ5="green" #Bouton zone 5 vert
#cadPZ1="red"
#cadPZ2="red"
#cadPZ3="red"
#cadPZ4="red"
#cadPZ5="red"
#----------------------------------

#Nombre durée (Manuel - Programmé)

#nDM = "05" #Manuel
#nDP = "05" #Programmé

#---------------------------------

#Nombre Horaire (Heure / Minutes)

#nH = "  0" #Heure
#nM = "00" #Minutes

#---------------------------------

lTH100=[0,1,2,3,4] #Gouttes [100;75]
lTH75=[0,1,2,3,4] #Gouttes ]75;50]
lTH50=[0,1,2,3,4] #Gouttes ]50;25]
lTH25=[0,1,2,3,4] #Gouttes ]25;0]
lPTH=[0,1,2,3,4] #Label Taux 
nPTH=[0,1,2,3,4] #Nombre Taux

#-------------------------------

eDZ=[0,1,2,3,4]
iEDZ=[0,1,2,3,4]
sEDZ=[0,1,2,3,4]

#--------------------------------
#######  COORDONEE BOUTONS  ###########################################################################################################################################################

def bp1(): #Place le bouton 1
    b1.place(x=10, y=10)
def bp2(): #Place le bouton 2
    b2.place(x=10, y=88)
def bp3(): #Place le bouton 3
    b3.place(x=10, y=166)
def bp4(): #Place le bouton 4
    b4.place(x=10, y=244)
def bp5(): #Place le bouton 5
    b5.place(x=10, y=322)
def bp6(): #Place le bouton 6
    b6.place(x=730, y=330)
def pec(): #Place la fenêtre "Page en cours"
    pageEnCours.place(x=272, y=18)

#######  (ACQUIRE)  ###################################################################################################################################################################

def acquire():
    acquire_vCapteurs()
    acquire_vArrosageManuel()
    acquire_vArrosageProgramme()
    acquire_vArrosageHumidite()
    acquire_sDescZones()
    acquire_vSecheresse()

def acquire_vCapteurs(): # température, humidite, temperature min/max, pluie
    with open("data/vCapteurs.txt", "r") as vCapteurs:
        for line in vCapteurs.readlines():
            exec(line, globals())
            print (line)
        nPTH[0]=humiditeZ1 #Humidité zone 1
        nPTH[1]=humiditeZ2 #Humidité zone 2
        nPTH[2]=humiditeZ3 #Humidité zone 3
        nPTH[3]=humiditeZ4 #Humidité zone 4
        nPTH[4]=humiditeZ5 #Humidité zone 5
        print(nPTH)

def acquire_vArrosageManuel(): # activé, zones, durée
    with open("data/vArrosageManuel.txt","r") as vArrosageManuel:
        for line in vArrosageManuel.readlines():
            exec(line, globals())
            print (line)

def acquire_vArrosageProgramme(): # activé, zones, duré, heure, minutes
    with open("data/vArrosageProgramme.txt","r") as vArrosageProgramme:
        for line in vArrosageProgramme.readlines():
            exec(line, globals())
            print (line)

def acquire_vArrosageHumidite(): # activé
    with open("data/vArrosageHumidite.txt","r") as vArrosageHumidite:
        for line in vArrosageHumidite.readlines():
            exec(line, globals())
            print (line)

def acquire_vSecheresse():
    with open("data/vSecheresse.txt","r") as vSecheresse:
        for line in vSecheresse.readlines():
            exec(line, globals())
            print (line)

def acquire_sDescZones():
    with open("data/sDescZones.txt","r") as sDescZones:
        for line in sDescZones.readlines():
            exec(line, globals())
            print (line)


#######  CLEAN GRAPH  ###################################################################################################################################################################

def cleanGraph():           #Commune à tout Efface la partie "graph"
    #accueil--------------
    cleanGraphAccueil()
    cleanGraphZones()
    cleanGraphDuree()
    cleanGraphHoraire()
    cleanGraphTauxHumidite()
    cleanGraphConditionsMeteo()
    cleanGraphDZones()
    cleanGraphProgrammesArrosage()
    cleanGraphReglages()
    #----------------------


#######  ACCUEIL  ###################################################################################################################################################################


#------------------------Veille-----------------------------------------Veille------------------------------------------------
def sortieVeille():         #De veille à accueil
    ecranVeille.place_forget()
    pec()#pageEnCours
    accueil()

def veille():               #Vider l'écran sous la veille
    cleanGraph()
    pageEnCours.place_forget()
    ecranVeille.place(x=0, y=0)

#--------------------------Partie Graphique---------------------------------------Partie Graphique---------------------------------------
#------------------------Programme en cours(label)-----------------------------------------Programme en cours(label)------------------

def labelProgrammeEnCours():                                # Choisis d'afficher humidité + programmé, humidité, programmé, ou aucuns des deux dans le label(milieu bas) de l'accueil
    if  arrosageHumiditeActif == 0 and arrosageProgrammeActif == 0:
        infoPA.config(image=h0p0,bg="black")
    elif arrosageHumiditeActif == 0 and arrosageProgrammeActif == 1:
        infoPA.config(image=h0p1,bg="green")
    elif arrosageHumiditeActif == 1 and arrosageProgrammeActif == 0:
        infoPA.config(image=h1p0,bg="green")
    else:
        infoPA.config(image=h1p1,bg="green")
    infoPA.place(x=185, y=340)

def iconeSecheresse():                                  #Choisis d'afficher ou non l'icone "Secheresse" si celle-ci est active
    if secheresseActif == 1:
        infoS.place(x=720,y=10)
    else:
        infoS.place_forget()

def pecAccueil():                                       #Label de page en cours
    pageEnCours.config(image=ipecAccueil)
    pec()


#-----------GRAPH ACCUEIL-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def cleanGraphAccueil():
    global acceuilActif
    infoPA.place_forget()
    infoS.place_forget()
    imageAccueil.place_forget()
    acceuilActif=0

def graphAccueil(): #Affiche la partie graph de l'accueil
    labelProgrammeEnCours() #Label (mileu-bas)
    iconeSecheresse() #Icone secheresse
    pecAccueil() #Page en cours
    imageAccueil.place(x=200, y=75) #Image centrale accueil


#--------------------------------------------------------------------------------------------------------------------------

def accueilB1():
    if secheresseActif == 0:    #Contour rouge au bouton "Programme d'arrosage" si secheresseActif=1
        b1.config(image=pa, bg="#7c7c7c", activebackground="#7c7c7c", command=programmeArrosage) #Programme d'arrosage
        bp1()
    else:
        b1.config(image=pa, bg="red", activebackground="red", command=accueil) #Programme d'arrosage
        bp1()

def accueil():
    global acceuilActif

    cleanGraph() #Clean la partie graph
    
    accueilB1()

    b2.config(image=m, bg="#7c7c7c", activebackground="#7c7c7c", command=meteo) #Météo
    bp2()
    
    b3.config(image=th, bg="#7c7c7c", activebackground="#7c7c7c", command=tauxHumidite) #Taux d'humidité
    bp3()
    
    b4.config(image=re, bg="#7c7c7c", activebackground="#7c7c7c", command=reglages) #Réglages
    bp4()
    
    b5.config(image=ac, bg="#7c7c7c", activebackground="#7c7c7c", command=accueil) #Accueil
    bp5()

    b6.config(image=ve, bg="#7c7c7c", activebackground="#7c7c7c", command=veille) #Veille
    bp6()

    graphAccueil() #Affiche la partie graph de l'accueil

    acceuilActif=1

########  PROGRAMME D'ARROSAGE  ########################################################################################################################################################

def cleanGraphProgrammesArrosage():
    lImageAide.place_forget()
    lImageManuel.place_forget()
    lImageProgramme.place_forget()
    lImageHumidite.place_forget()
    lMpm.place_forget()
    lSelectZoneSVP.place_forget()

def pecProgrammeArrosage(): #Programme en cours "ProgrammeArrosage"
    pageEnCours.config(image=ipecProgrammeArrosage)
    pec()

#-----------GRAPH PROGRAMME D'ARROSAGE---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def graphProgrammeArrosage():   #Affiche la partie graph de "ProgrammeArrosage"
    pecProgrammeArrosage()
    lImageAide.place(x=238, y=102)

#-----------PROGRAMME D'ARROSAGE------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def programmeArrosage(): #Blocage de la section programme d'arrosage si secheresseActif=1

    if secheresseActif == 0:

        cleanGraph()  #Clean la partie graph

        b1.config(image=am, bg="#7c7c7c", activebackground="#7c7c7c", command=arrosageManuel)  #Arrosage manuel
        bp1()
    
        b2.config(image=ap, bg="#7c7c7c", activebackground="#7c7c7c", command=arrosageProgramme)  #Arrosage programmé
        bp2()
    
        b3.config(image=ah, bg="#7c7c7c", activebackground="#7c7c7c",command=arrosageHumidite)  #Arrosage humidité
        bp3()
    
        b4.place_forget() #_
    
        b5.config(image=ac, bg="#7c7c7c", activebackground="#7c7c7c", command=accueil) #Accueil
        bp5()

        b6.place_forget() #_ 

        graphProgrammeArrosage() #Affiche la partie graph de "Programme d'arrosage"

    else:
        accueil()

#######  ARROSAGE MANUEL  #############################################################################################################################################################

def pecManuel(): #Programme en cours "Arrosage manuel"
    pageEnCours.config(image=ipecManuel)
    pec()

#-----------GRAPH ARROSAGE MANUEL-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def graphManuel(): #Affiche la partie graph de "Arrosage manuel"
    pecManuel()
    if temps == 4:
        lMpm.place(x=188, y=130)
    else:
        lImageManuel.place(x=245, y=141)

#-----------ARROSAGE MANUEL-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def ecrire_vArrosageManuel():
    with open("data/vArrosageManuel.txt","w") as file: #Réécriture du fichier avec les nouvelles valeurs
        file.write("arrosageManuelActif="+str(arrosageManuelActif)+"\nmZ1="+str(mZ1)+"\nmZ2="+str(mZ2)+"\nmZ3="+str(mZ3)+"\nmZ4="+str(mZ4)+"\nmZ5="+str(mZ5)+"\nnDM="+str(int(nDM))+"\n")


def vManuel(): #vaidation de l'arrosage manuel
    
    global arrosageManuelActif
    if mZ1 or mZ2 or mZ3 or mZ4 or mZ5 == 1:
        arrosageManuelActif = 1 #Activation de l'arrosage manuel
        ecrire_vArrosageManuel()
        arrosageManuel() #Retour au menu arrosage manuel
        b3.config(image=vActif,bg="#007600", activebackground="#007600") #Bouton "validé" en vert
    else:
        arrosageManuelActif = 0
        ecrire_vArrosageManuel()
        arrosageManuel()
        lImageManuel.place_forget()
        lMpm.place_forget()
        lSelectZoneSVP.place(x=229, y=111)

def arrosageManuel():
    
    cleanGraph()  #Clean la partie graph

    b1.config(image=cz, bg="#7c7c7c", activebackground="#7c7c7c", command=graphZonesManuel) #Choix des zones
    bp1()
    
    b2.config(image=du, bg="#7c7c7c", activebackground="#7c7c7c", command=graphDureeManuel) #Durée
    bp2()
    
    b3.config(image=v, bg="#7c7c7c", activebackground="#7c7c7c", command=vManuel) #Valider
    bp3()
    
    b4.place_forget() #_
    
    b5.config(image=r, bg="#7c7c7c", activebackground="#7c7c7c", command=programmeArrosage) #Retour
    bp5()

    b6.place_forget() #_ 

    graphManuel() #Affiche la partie graph de "Arrosage manuel"

    acquire_vArrosageManuel()

#######  ARROSAGE PROGRAMME  ###########################################################################################################################################################

#---Désactiver arrosageProgramme si changement---

def changeP(): #Désactive arrosageProgramme si changement
    global arrosageProgrammeActif

    if arrosageProgrammeActif==1:
        arrosageProgrammeActif=0
    ecrire_vArrosageProgramme()    
    arrosageProgrammeB4()


#---arrosageProgramme Desactiver / Activer---

def ecrire_vArrosageProgramme():
    with open("data/vArrosageProgramme.txt","w") as file: #Réécriture du fichier avec les nouvelles valeurs
        file.write("arrosageProgrammeActif="+str(arrosageProgrammeActif)+"\npZ1="+str(pZ1)+"\npZ2="+str(pZ2)+"\npZ3="+str(pZ3)+"\npZ4="+str(pZ4)+"\npZ5="+str(pZ5)+"\nnDP="+str(int(nDP))+"\nnH="+str(int(nH))+"\nnM="+str(int(nM))+"\n")

def arrosageProgrammeAD():                #Change arrosageProgrammeActif quand pression de B4
    global arrosageProgrammeActif
    if pZ1 or pZ2 or pZ3 or pZ4 or pZ5 == 1:
        if arrosageProgrammeActif==0:
            arrosageProgrammeActif=1
        else:
            arrosageProgrammeActif=0
    else:
        arrosageMProgrammeActif = 0
        ecrire_vArrosageProgramme()
        arrosageProgramme()
        lImageProgramme.place_forget()
        lSelectZoneSVP.place(x=229, y=111)
    ecrire_vArrosageProgramme()
    arrosageProgrammeB4()

#--------------------------------------------------

def pecProgramme(): #Programme en cours "Arrosage programmé"
    pageEnCours.config(image=ipecProgramme)
    pec()

#-----------GRAPH ARROSAGE PROGRAMME-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def graphProgramme(): #Affiche la partie graph de "Arrosage programmé"
    pecProgramme()
    lImageProgramme.place(x=245, y=141)

#-----------ARROSAGE PROGRAMME-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def arrosageProgrammeB4():                                            #Activer/Désactiver
    acquire_vArrosageProgramme()
    print ("COUCOU")
    if arrosageProgrammeActif==1:
        b4.config(image=dacti)
    else:
        b4.config(image=acti)
    bp4()

def arrosageProgramme():

    cleanGraph()  #Clean la partie graph

    b1.config(image=cz, bg="#7c7c7c", activebackground="#7c7c7c", command=graphZonesProgramme) #Choix des zones
    bp1()
    
    b2.config(image=du, bg="#7c7c7c", activebackground="#7c7c7c", command=graphDureeProgramme) #Durée
    bp2()
    
    b3.config(image=h, bg="#7c7c7c", activebackground="#7c7c7c", command=graphHoraire) #Horaire
    bp3()
    
    b4.config(bg="#7c7c7c", activebackground="#7c7c7c", command=arrosageProgrammeAD)
    arrosageProgrammeB4()

    b5.config(image=r, bg="#7c7c7c", activebackground="#7c7c7c",command=programmeArrosage) #Retour a "Programme d'arrosage"
    bp5()

    b6.place_forget() #_

    graphProgramme() #Affiche la partie graph de "Arrosage programmé"

    acquire_vArrosageProgramme()

########  ARROSAGE HUMIDITE  ###########################################################################################################################################################

#---arrosageHumidite Desactiver / Activer---

def ecrire_vArrosageHumidite():
    with open("data/vArrosageHumidite.txt","w") as file: #Réécriture du fichier avec les nouvelles valeurs
        file.write("arrosageHumiditeActif="+str(arrosageHumiditeActif)+"\n")

def arrosageHumiditeAD():              #Change arrosageHumiditeActif quand pression de B2
    global arrosageHumiditeActif

    if arrosageHumiditeActif == 1:
        arrosageHumiditeActif=0
    else:
        arrosageHumiditeActif=1
    ecrire_vArrosageHumidite()
    arrosageHumiditeB2()

#----------------------------------------------

def pecHumidite(): #Programme en cours "Arrosage humidité"
    pageEnCours.config(image=ipecHumidite)
    pec()

#-----------GRAPH HUMIDITE-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def graphHumidite(): #Affiche la partie graph de "Arrosage humidité"
    pecHumidite()
    lImageHumidite.place(x=245, y=141)

#-----------ARROSAGE HUMIDITE-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def arrosageHumiditeB2():                                                      #Activer/Désactiver
    acquire_vArrosageHumidite()
    if arrosageHumiditeActif == 1:
        b2.config(image=dacti) #Désactiver
    else:
        b2.config(image=acti) #Activer
    bp2()

def arrosageHumidite():
    
    cleanGraph()  #Clean la partie graph

    b1.place_forget() #_

    b2.config(bg="#7c7c7c", activebackground="#7c7c7c", command=arrosageHumiditeAD)
    arrosageHumiditeB2()                                                        #Activer/Désactiver

    b3.place_forget() #_

    b4.place_forget() #_

    b5.config(image=r, bg="#7c7c7c", activebackground="#7c7c7c",command=programmeArrosage) #Retour a "Programme d'arrosage"
    bp5()

    b6.place_forget() #_ 

    graphHumidite() #Affiche la partie graph de "Arrosage humidité"

#######  METEO  ####################################################################################################################################################################

def pecMeteo(): #Programme en cours "Météo"
    pageEnCours.config(image=ipecMeteo)
    pec()
#-----------GRAPH METEO-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def graphMeteo(): #Affiche la partie graph de "Météo"
    pecMeteo()
    iconeSecheresse() #Icone secheresse
    gaphConditionsMeteo()

#-----------METEO-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def meteo():
    
    cleanGraph()  #Clean la partie graph

    b6.config(image=act,command=gaphConditionsMeteo) #Actualiser
    bp6()

    graphMeteo() #Affiche la partie graph de "Météo"

#######  TAUX D'HUMIDITE  ##############################################################################################################################################################

def pecTauxHumidite(): #Programme en cours "Taux d'humidité"
    pageEnCours.config(image=ipecTauxHumidite)
    pec()

#-----------GRAPH TAUX D'HUMIDITE-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def graphTauxHumidite(): #Affiche la partie graph de "Taux d'humidité"
    pecTauxHumidite()
    iconeSecheresse() #Icone secheresse
    zonesTauxHumidite()

#-----------TAUX D'HUMIDITE-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def tauxHumidite():

    cleanGraph()  #Clean la partie graph

    b6.config(image=act,command=zonesTauxHumidite) #Actualiser
    bp6()

    graphTauxHumidite() #Affiche la partie graph de "Taux d'humidité"


#######  REGLAGES  ###################################################################################################################################################################

def cleanGraphReglages():
    lImageReglages.place_forget()

#----------Desc zones---------------------------------------------------------------Nom zones-------------------------------------

def ecrire_sDescZones():
    with open("data/sDescZones.txt","w") as file: #Réécriture du fichier avec les nouvelles valeurs
        file.write("iEDZ[0]= " + "'" + iEDZ[0] + "'" + "\n" + "iEDZ[1]= " + "'" + iEDZ[1] + "'" + "\n" + "iEDZ[2]= " + "'" + iEDZ[2] + "'" + "\n" + "iEDZ[3]= " + "'" + iEDZ[3] + "'" + "\n" + "iEDZ[4]= " + "'" + iEDZ[4] + "'" + "\n")


def pecDZones(): #Programme en cours "Nom Zones"
    pageEnCours.config(image=ipecDZones)
    pec()

def okDZ():
    for i in range(0,5):
        iEDZ[i] = eDZ[i].get()
        iEDZ[i] = iEDZ[i].replace("'","`")
        iEDZ[i] = iEDZ[i].replace('"',"``")
    b6.config(image=edit, command=editDZ)
    ecrire_sDescZones()
    insertDZ()

def editDZ():
    for i in range(0,5):
        eDZ[i].config(state=NORMAL)
    b6.config(image=ok, command=okDZ)

#-----------Desc ZONES-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def dZones():

    cleanGraph()  #Clean la partie graph

    b1.place_forget() #_

    b2.place_forget() #_

    b3.place_forget() #_

    b4.place_forget() #_

    b5.config(image=r, bg="#7c7c7c", activebackground="#7c7c7c", command=reglages) #Retour
    bp5()

    b6.config(image=edit, command=editDZ)
    bp6()

    graphDZones() #Affiche la partie graph de "DescZones"
    
    pecDZones()
#------------------------------------------------------------------------------------------------------------------------------------

def pecReglages():  #Programme en cours "Réglages"
    pageEnCours.config(image=ipecReglages)
    pec()

#-----------GRAPH REGLAGES-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def graphReglages(): #Affiche la partie graph de "Réglages"
    pecReglages()
    lImageReglages.place(x=328, y=105)

#-----------REGLAGES-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#-------------Secheresse--------------------------------------------------------secheresse----------------------

#---secheresse Desactiver / Activer---

def ecrire_vSecheresse():
    with open("data/vSecheresse.txt","w") as file: #Réécriture du fichier avec les nouvelles valeurs
        file.write("secheresseActif= " + str(secheresseActif) + "\n" + "asp= " + str(asp)  + "\n" + "sArrosageProgrammeActif= " + str(sArrosageProgrammeActif) + "\n" + "sArrosageHumiditeActif= " + str(sArrosageHumiditeActif) + "\n")

def secheresseAD():     #Change secheresseActif quand pression de B1
    global secheresseActif, arrosageProgrammeActif, sArrosageProgrammeActif, arrosageHumiditeActif, sArrosageHumiditeActif, sdu

    if secheresseActif==0:              #Sauvegarde arrosage avant la secheresse
        secheresseActif=1
        sArrosageProgrammeActif = arrosageProgrammeActif
        sArrosageHumiditeActif = arrosageHumiditeActif
        arrosageProgrammeActif = 0
        arrosageHumiditeActif = 0
        sdu=1
    else:                               #Réactivage des programmes d'arrosage après secheresse
        secheresseActif=0
        arrosageProgrammeActif = sArrosageProgrammeActif
        arrosageHumiditeActif = sArrosageHumiditeActif
    ecrire_vSecheresse()
    ecrire_vArrosageProgramme
    ecrire_vArrosageHumidite
    reglagesB1()

#---secheresse affichage---

def reglagesB1():
    
    if secheresseActif == 0:
        b1.config(image=sa, bg="#7c7c7c", activebackground="#7c7c7c", command=secheresseAD) #Activer
    else:
        b1.config(image=sd, bg="#7c7c7c", activebackground="#7c7c7c", command=secheresseAD) #Désactiver
    bp1()

def reglages():

    cleanGraph()  #Clean la partie graph

    acquire_vSecheresse()

    reglagesB1() #Change secheresseActif quand pression de B1
    
    b2.config(image=dz, bg="#7c7c7c", activebackground="#7c7c7c", command=dZones) #Nom zones : Claver necessaire
    bp2()
    
    b3.place_forget()

    b4.place_forget()
    
    b5.config(image=ac, bg="#7c7c7c", activebackground="#7c7c7c", command=accueil) #Accueil
    bp5()

    b6.place_forget() #_

    graphReglages() #Affiche la partie graph de "Réglages"

#################################################################################################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################

#  PARTIE GRAPHIQUE  PARTIE GRAPHIQUE  PARTIE GRAPHIQUE  PARTIE GRAPHIQUE  PARTIE GRAPHIQUE  PARTIE GRAPHIQUE  PARTIE GRAPHIQUE  PARTIE GRAPHIQUE  PARTIE GRAPHIQUE  PARTIE GRAPHIQUE

############  GRAPH NOM ZONES  ##################################################################################################################################################

def cleanGraphZones():  #Efface la partie graph de choix des zones pour l'arrosage manuel et programmé
        bZ1.place_forget()
        bZ2.place_forget()
        bZ3.place_forget()
        bZ4.place_forget()
        bZ5.place_forget()

#Manuel------------------------------------------------------------------------------------------------------------------------

def graphZonesManuel():     #Changement de couleur des boutons "Zones" pour l'arrosage manuel + assignement de zZ[x] de 0 a 1

    def cMZ1(): #Active la zone 1 pour l'arrosage manuel
        global mZ1
        if mZ1==0: #Changement de la variable mZ1
            mZ1=1
        else:
            mZ1=0
        couleurBoutonZonesManuel() #Changement de la couleur du bouton de zone en fonction de mZ[i]
        bZ1.config(bg=cadMZ1) #Affichage de la couleur
        

    def cMZ2(): #Active la zone 2 pour l'arrosage manuel
        global mZ2
        if mZ2==0:
            mZ2=1
        else:
            mZ2=0
        couleurBoutonZonesManuel()
        bZ2.config(bg=cadMZ2)
        
    def cMZ3(): #Active la zone 3 pour l'arrosage manuel
        global mZ3
        if mZ3==0:
            mZ3=1
        else:
            mZ3=0
        couleurBoutonZonesManuel()
        bZ3.config(bg=cadMZ3)

    def cMZ4(): #Active la zone 4 pour l'arrosage manuel
        global mZ4
        if mZ4==0:
            mZ4=1
        else:
            mZ4=0
        couleurBoutonZonesManuel()
        bZ4.config(bg=cadMZ4)

    def cMZ5(): #Active la zone 5 pour l'arrosage manuel
        global mZ5
        if mZ5==0:
            mZ5=1
        else:
            mZ5=0
        couleurBoutonZonesManuel()
        bZ5.config(bg=cadMZ5)

    b1.config(bg="yellow") #Selection de choix zones 
    b2.config(bg="#7c7c7c") #déselection de choix durée
    b3.config(image=v, bg="#7c7c7c", activebackground="#7c7c7c") #Réinitialistaion du bouton validé vers valider
    cleanGraph() #Efface la partie graph
    couleurBoutonZonesManuel() #Initialisation des couleur en fonction de mZ[i]
    bZ1.config(bg=cadMZ1, command=cMZ1) #Initialisation du bouton Zone 1 pour choix "manuel"
    bZ1.place(x=242,y=96)#Placement du bouton Zone 1
    bZ2.config(bg=cadMZ2, command=cMZ2) #Initialisation du bouton Zone 2 pour choix "manuel"
    bZ2.place(x=402,y=96)#Placement du bouton Zone 2
    bZ3.config(bg=cadMZ3, command=cMZ3) #Initialisation du bouton Zone 3 pour choix "manuel"
    bZ3.place(x=562,y=96)#Placement du bouton Zone 3
    bZ4.config(bg=cadMZ4, command=cMZ4) #Initialisation du bouton Zone 4 pour choix "manuel"
    bZ4.place(x=322,y=248)#Placement du bouton Zone 4
    bZ5.config(bg=cadMZ5, command=cMZ5) #Initialisation du bouton Zone 5 pour choix "manuel"
    bZ5.place(x=480,y=248)#Placement du bouton Zone 5

#Programmé------------------------------------------------------------------------------------------------------------------------

def graphZonesProgramme():      #Changement de couleur des boutons "Zones" pour l'arrosage programmé + assignement de pZ[x] de 0 a 1

    def cPZ1(): #Active la zone 1 pour l'arrosage programmé
        changeP() #Désactive arrosageProgramme si changement
        global pZ1
        if pZ1==0:
            pZ1=1
        else:
            pZ1=0
        couleurBoutonZonesProgramme()
        bZ1.config(bg=cadPZ1)

    def cPZ2(): #Active la zone 2 pour l'arrosage programmé
        changeP() #Désactive arrosageProgramme si changement
        global pZ2
        if pZ2==0:
            pZ2=1
        else:
            pZ2=0
        couleurBoutonZonesProgramme()
        bZ2.config(bg=cadPZ2)

    def cPZ3(): #Active la zone 3 pour l'arrosage programmé
        changeP() #Désactive arrosageProgramme si changement
        global pZ3
        if pZ3==0:
            pZ3=1
        else:
            pZ3=0
        couleurBoutonZonesProgramme()
        bZ3.config(bg=cadPZ3)

    def cPZ4(): #Active la zone 4 pour l'arrosage programmé
        changeP() #Désactive arrosageProgramme si changement
        global pZ4
        if pZ4==0:
            pZ4=1
        else:
            pZ4=0
        couleurBoutonZonesProgramme()
        bZ4.config(bg=cadPZ4)

    def cPZ5(): #Active la zone 5 pour l'arrosage programmé
        changeP() #Désactive arrosageProgramme si changement
        global pZ5
        if pZ5==0:
            pZ5=1
        else:
            pZ5=0
        couleurBoutonZonesProgramme()
        bZ5.config(bg=cadPZ5)

    b1.config(bg="yellow") #Selection de choix zones 
    b2.config(bg="#7c7c7c") #déselection de choix durée
    b3.config(bg="#7c7c7c") #déselection de choix horaire
    cleanGraph() #Efface la partie graph
    couleurBoutonZonesProgramme() #Initialisation des couleur en fonction de mZ[i]
    bZ1.config(bg=cadPZ1, command=cPZ1) #Initialisation du bouton Zone 1 pour choix "programmé"
    bZ1.place(x=242,y=96) #Placement du bouton Zone 1
    bZ2.config(bg=cadPZ2, command=cPZ2) #initialisation du bouton Zone 2 pour choix "programmé"
    bZ2.place(x=402,y=96) #Placement du bouton Zone 2
    bZ3.config(bg=cadPZ3, command=cPZ3) #Initialisation du bouton Zone 3 pour choix "programmé"
    bZ3.place(x=562,y=96) #Placement du bouton Zone 3
    bZ4.config(bg=cadPZ4, command=cPZ4) #Initialisation du bouton Zone 4 pour choix "programmé"
    bZ4.place(x=322,y=248) #Placement du bouton Zone I
    bZ5.config(bg=cadPZ5, command=cPZ5) #Initialisation du bouton Zone 5 pour choix "programmé"
    bZ5.place(x=480,y=248) #Placement du bouton Zone 5

############  GRAPH DUREE  ##################################################################################################################################################

def cleanGraphDuree():  #Efface la partie graph de choix de la durée d'arrosage pour l'arrosage manuel et programmé
    bFlecheBas.place_forget()
    bFlecheHaut.place_forget()
    lXMinutes.place_forget()
    bP10Haut.place_forget()
    bP10Bas.place_forget()
    nombreDuree.place_forget()

#Manuel---------------------------------------------------------------------------------------------------------------------------

def graphDureeManuel(): #Changement de la durée pour l'arrosage manuel + assignement de nDM
    global nDM
    def cMDH(): #Augmente la durée de 1 
        global nDM
        nDM = int(nDM)
        if nDM >= 60: #Max 60
            nDM = 60 #Max 60
        else: 
            nDM = nDM + 1
        if nDM < 10:    #ajout "0" devant si < 10
            nDM = str(nDM)
            nDM = "0" + nDM
        nombreDuree.config(text=nDM)
    
    def cMDH10(): #Augmente la durée de 10
        global nDM
        nDM = int(nDM)
        if nDM >= 50: #Max 60
            nDM = 60 #Max 60
        else: 
            nDM = nDM + 10
        if nDM < 10:    #ajout "0" devant si < 10
            nDM = str(nDM)
            nDM = "0" + nDM
        nombreDuree.config(text=nDM)
    
    def cMDB(): #Diminue la durée de 1
        global nDM
        nDM = int(nDM)
        if nDM <= 5: #Min 5
            nDM = 5 #Min 5
        else:
            nDM = nDM - 1
        if nDM < 10:    #ajout "0" devant si < 10
            nDM = str(nDM)
            nDM = "0" + nDM
        nombreDuree.config(text=nDM)
    
    def cMDB10(): #Diminue la durée de 10
        global nDM
        nDM = int(nDM)
        if nDM <= 15: #Min 5
            nDM = 5 #Min 5
        else: 
            nDM = nDM - 10
        if nDM < 10:    #ajout "0" devant si < 10
            nDM = str(nDM)
            nDM = "0" + nDM
        nombreDuree.config(text=nDM)
    
    b1.config(bg="#7c7c7c")
    b2.config(bg="yellow")
    b3.config(image=v, bg="#7c7c7c", activebackground="#7c7c7c")
    cleanGraph() #Efface la partie graph
    lXMinutes.place(x=300, y=147) #Affiche fenêtre centrale "minutes"
    bFlecheHaut.config(command=cMDH) #Initialisation Bouton +1
    bFlecheHaut.place(x=593, y=147) #Placement Bouton +1
    bP10Haut.config(command=cMDH10) #Initialisation Bouton +10
    bP10Haut.place(x=528, y=147) #Placement Bouton +10
    bFlecheBas.config(command=cMDB) #Initialisation Bouton -1
    bFlecheBas.place(x=593, y=220) #Placement Bouton -1
    bP10Bas.config(command=cMDB10) #Initialisation Bouton -10
    bP10Bas.place(x=528,y=220) #Placement Bouton -10
    nDM = int(nDM)
    if int(nDM) < 10:
        nDM = "0" + str(nDM)
    nombreDuree.config(text=nDM, font=policeNombreDurée) #Chiffre a afficher dans la fenêtre centrale "minutes"
    nombreDuree.place(x=375, y=187) #Affichage du chiffre

#Programmé---------------------------------------------------------------------------------------------------------------------------

def graphDureeProgramme():  #Changement de la durée pour l'arrosage manuel + assignement de nDP
    global nDP

    def cPDH(): #Augmente la durée de 1
        changeP() #Désactive arrosageProgramme si changement
        global nDP
        nDP = int(nDP)
        if nDP >= 60: #Max 60
            nDP = 60 #Max 60
        else: 
            nDP = nDP + 1
        if nDP < 10:    #ajout "0" devant si < 10
            nDP = str(nDP)
            nDP = "0" + nDP
        nombreDuree.config(text=nDP)
    
    def cPDH10(): #Augmente la durée de 10
        changeP() #Désactive arrosageProgramme si changement
        global nDP
        nDP = int(nDP)
        if nDP >= 50: #Max 60
            nDP = 60 #Max 60
        else: 
            nDP = nDP + 10
        if nDP < 10:    #ajout "0" devant si < 10
            nDP = str(nDP)
            nDP = "0" + nDP
        nombreDuree.config(text=nDP)
    
    def cPDB(): #Diminue la durée de 1
        changeP() #Désactive arrosageProgramme si changement
        global nDP
        nDP = int(nDP)
        if nDP <= 5: #Min 5
            nDP = 5 #Min 5
        else:
            nDP = nDP - 1
        if nDP < 10:    #ajout "0" devant si < 10
            nDP = str(nDP)
            nDP = "0" + nDP
        nombreDuree.config(text=nDP)
    
    def cPDB10(): #Diminue la durée de 10
        changeP() #Désactive arrosageProgramme si changement
        global nDP
        nDP = int(nDP)
        if nDP <= 15: #Min 5
            nDP = 5 #Min 5
        else: 
            nDP = nDP - 10
        if nDP < 10:    #ajout "0" devant si < 10
            nDP = str(nDP)
            nDP = "0" + nDP
        nombreDuree.config(text=nDP)
    
    b1.config(bg="#7c7c7c")
    b2.config(bg="yellow")
    b3.config(bg="#7c7c7c")
    cleanGraph() #Efface la partie graph
    lXMinutes.place(x=300, y=147) #Affiche fenêtre centrale "minutes"
    bFlecheHaut.config(command=cPDH) #Initialisation Bouton +1
    bFlecheHaut.place(x=593, y=147) #Placement Bouton +1
    bP10Haut.config(command=cPDH10) #Initialisation Bouton +10
    bP10Haut.place(x=528, y=147) #Placement Bouton +10
    bFlecheBas.config(command=cPDB) #Initialisation Bouton -1
    bFlecheBas.place(x=593, y=220) #Placement Bouton -1
    bP10Bas.config(command=cPDB10) #Initialisation Bouton -10
    bP10Bas.place(x=528,y=220) #Placement Bouton -10
    nDP=int(nDP)
    if int(nDP) < 10:
        nDP= "0" + str(nDP)
    nombreDuree.config(text=nDP, font=policeNombreDurée) #Chiffre a afficher dans la fenêtre centrale "minutes"
    nombreDuree.place(x=375, y=187) #Affichage du chiffre

############  GRAPH HORAIRE  ##################################################################################################################################################

def cleanGraphHoraire():    #Efface la partie graph de choix de l'horaire pour l'arrosage programmé
    bFlecheBas.place_forget()
    bFlecheHaut.place_forget()
    lXHoraire.place_forget()
    bSHeure.place_forget()
    bSMinutes.place_forget()
    hM.place_forget()
    hH.place_forget()
    policeHH.config(underline = False) #Désouligne nombre heure
    policeHM.config(underline = False) #Désouligne nombre minutes

#Heure---------------------------------------------------------------------------------------------------------------------------------

def hHeure():

    def cHHH(): #Augmente l'heure de 1
        changeP() #Désactive arrosageProgramme si changement
        global nH
        nH = int(nH)
        if nH >= 23: #Max 23
            nH = 0 #Reviens à 0
        else: 
            nH = nH + 1
        if nH < 10: #Ajoute un espace si < 10
            nH = "  " + str(nH)
        hH.config(text=nH)
    
    def cHHB(): #Diminue l'heure de 1
        changeP() #Désactive arrosageProgramme si changement
        global nH
        nH = int(nH)
        if nH <= 0: #Min 0
            nH = 23 #Revins à 23
        else:
            nH = nH - 1
        if nH < 10: #Ajoute un espace si < 10
            nH = "  " + str(nH)
        hH.config(text=nH)

    policeHH.config(underline = True) #Souligne nombre heure
    policeHM.config(underline = False) #Désouligne nombre minutes
    bFlecheHaut.config(command=cHHH) #Initialisation Bouton +1
    bFlecheBas.config(command=cHHB) #Initialisation Bouton -1

#Minutes---------------------------------------------------------------------------------------------------------------------------------

def hMinutes():

    def cHMH(): #Augmente les minutes de 10
        changeP() #Désactive arrosageProgramme si changement
        global nM
        nM = int(nM)
        if nM >= 40: #Min 0
            nM = 50 #Min 0
        else: 
            nM = int(nM) + 10
        if nM < 10: #ajout "0" devant si < 10
            nM = "0" + str(nM)
        hM.config(text=nM)
    
    def cHMB(): #Diminue les minutes de 10
        changeP() #Désactive arrosageProgramme si changement
        global nM
        nM = int(nM)
        if nM <= 10: #Min 0
            nM = 0 #Min 0
        else:
            nM = int(nM) - 10
        if nM < 10: #ajout "0" devant si < 10
            nM = "0" + str(nM)
        hM.config(text=nM)

    policeHH.config(underline = False) #Désouligne nombre heure
    policeHM.config(underline = True) #souligne nombre minutes
    bFlecheHaut.config(command=cHMH) #Initialisation Bouton +1
    bFlecheBas.config(command=cHMB) #Initialisation Bouton -1

#-------------------------------------------------------------------------------------------------------------------------------------------

def graphHoraire():
    global nM, nH

    b1.config(bg="#7c7c7c") #Couleur bouton 1 normale
    b2.config(bg="#7c7c7c") #Couleur bouton 2 normale
    b3.config(bg="yellow") #Couleur bouton 3 selection
    cleanGraph() #Clean la partie graph
    lXHoraire.place(x=320, y=147) #Affiche fenêtre centrale "minutes"
    bSHeure.place(x=310, y=329) #Affiche le bouton de selection de l'heure
    bSMinutes.place(x=522, y=329) #Affiche le bouton de selection des minutes
    bFlecheHaut.place(x=573, y=147) #Placement Bouton +1
    bFlecheBas.place(x=573, y=220) #Placement Bouton -1
    nH=int(nH)
    nM=int(nM)
    if int(nH) < 10:
        nH = "  " + str(nH)
    hH.config(text=nH)
    hH.place(x=365, y=187) #Affiche le nombre d'heures
    if int(nM) < 10:
        nM = "0" + str(nM)
        if int(nM) <= 0:
            nM = "00"
    hM.config(text=nM)
    hM.place(x=415, y=187) #Affiche le nombre de minutes
    hHeure() #Boot avec selection de l'heure

############  GRAPH TAUX HUMIDITE  ##################################################################################################################################################

def cleanGraphTauxHumidite(): #Efface la partie graph de Taux humidite
    for i in range(0,5):
        lTH100[i].place_forget() #Efface les gouttes
        lTH75[i].place_forget() #Efface les gouttes
        lTH50[i].place_forget() #Efface les gouttes
        lTH25[i].place_forget() #Efface les gouttes
        lPTH[i].place_forget() #Efface label pourcentage taux humidite
        lTH1.place_forget()
        lTH2.place_forget()
        lTH3.place_forget()
        lTH4.place_forget()
        lTH5.place_forget()

def choixGoutte(THx,px,py,n): #placement goutte + taux pour toutes les cases
    n=n-1 #liste = 0,1,2,3,4 n=1,2,3,4,5
    lTH100[n].place_forget() #Efface les gouttes
    lTH75[n].place_forget() #Efface les gouttes
    lTH50[n].place_forget() #Efface les gouttes
    lTH25[n].place_forget() #Efface les gouttes
    #Affichage goutte en fonction du TH------------
    if THx >= 75: 
        lTH100[n].place(x=px,y=py)
    elif THx >= 50:
        lTH75[n].place(x=px,y=py)
    elif THx >= 25:
        lTH50[n].place(x=px,y=py)
    elif THx < 25:
        lTH25[n].place(x=px,y=py)
    #Nombre taux d'humidite------------------------
    print (nPTH[n])
    if nPTH[n] < 10:
        nPTH[n]="    "+str(nPTH[n])
    elif nPTH[n] < 100:
        nPTH[n]="  "+str(nPTH[n])
    nPTH[n]=str(nPTH[n])+"%" #Ajout du %
    lPTH[n].config(text=nPTH[n])
    lPTH[n].place(x=px-70, y=py+31) #Placement du label en fonction des coord de la goutte

def zonesTauxHumidite():
    acquire_vCapteurs()
    lTH1.place(x=200, y=119)
    lTH2.place(x=398, y=119)
    lTH3.place(x=596, y=119)
    lTH4.place(x=300, y=250)
    lTH5.place(x=497, y=250)
    choixGoutte(humiditeZ1,296,141,1) #Goutte + taux zone 1
    choixGoutte(humiditeZ2,494,141,2) #Goutte + taux zone 2
    choixGoutte(humiditeZ3,692,141,3) #Goutte + taux zone 3
    choixGoutte(humiditeZ4,396,272,4) #Goutte + taux zone 4
    choixGoutte(humiditeZ5,593,272,5) #Goutte + taux zone 5

############  GRAPH METEO  ##################################################################################################################################################

def cleanGraphConditionsMeteo():
    lMTime.place_forget()
    lMTemp.place_forget()
    lTime.place_forget()
    lTemp.place_forget()
    lMTMax.place_forget()
    lTMax.place_forget()
    lMTMin.place_forget()
    lTMin.place_forget()
    lMCond.place_forget()

def timeAct():
    global timeAcq
    while 1:
        time.sleep(1)
        timeAcq=time.strftime("%H:%M")
        lTime.config(text=timeAcq)

def temperatureAcq():
    global temperature
    if -10 < int(temperature) < 0:
        temperature=" "+str(temperature)
    if 0 <= int(temperature) < 10:
        temperature="  "+str(temperature)
    temperature=str(temperature)+"°C"
    lTemp.config(text=temperature)

def tMaxAcq():
    global tempMax
    tempMax=str(tempMax)+"°C"
    lTMax.config(text=tempMax)

def tMinAcq():
    global tempMin
    tempMin=str(tempMin)+"°C"
    lTMin.config(text=tempMin)

def mCond():
    lMCond.place_forget()
    if temps<=3:
        if temps == 1:
            lMCond.config(image=sun)
            lMCond.place(x=466, y=74)
        if temps == 2:
            lMCond.config(image=sunCloud)
            lMCond.place(x=459, y=74)
        if temps == 3:
            lMCond.config(image=cloud)
            lMCond.place(x=466, y=104)
    else:
        if temps == 4:
            lMCond.config(image=rain)
            lMCond.place(x=466, y=104)
        if temps == 5:
            lMCond.config(image=snow)
            lMCond.place(x=466, y=104)
        if temps == 6:
            lMCond.config(image=storm)
            lMCond.place(x=466, y=104)

def gaphConditionsMeteo():
    acquire_vCapteurs()
    lMTime.place(x=220, y=270)
    lTime.place(x=250, y=300)
    lMTemp.place(x=220, y=130)
    lTemp.place(x=255, y=155)
    lMTMax.place(x=575, y=320)
    lTMax.place(x=630, y=342)
    lMTMin.place(x=425, y=320)
    lTMin.place(x=475, y=342)
    temperatureAcq()
    tMaxAcq()
    tMinAcq()
    mCond()

#############  GRAPH DESCRIPTION ZONES  ########################################################################################################################################################
#-----Limite caractere des Entry--------------------------------------------------

#---------------------------------------------------------------------------------

def cleanGraphDZones():
    lIDZ.place_forget()
    lWarnClavier.place_forget()
    for i in range(0,5):
        eDZ[i].place_forget()

def insertDZ():
    for i in range(0,5):
        eDZ[i].delete(0, END)
        eDZ[i].insert(0,iEDZ[i])
        eDZ[i].config(state=DISABLED)

def graphDZones(): #Affiche la partie graph de "Nom Zones"
    acquire_sDescZones()
    lIDZ.place(x=222, y=95)
    lWarnClavier.place(x=8, y=71)
    eDZ[0].place(x=335,y=104)
    eDZ[1].place(x=335,y=162)
    eDZ[2].place(x=335,y=220)
    eDZ[3].place(x=335,y=278)
    eDZ[4].place(x=335,y=336)
    insertDZ()
    okDZ()

#################################################################################################################################################################################
#################################################################################################################################################################################

acquire() #Acquisition des valeurs des fichiers txt

#############  BOOT ACCUEIL  ###########################################################################################################################################################

b1= Button(root, text="_", image=pa, bg="#7c7c7c", activebackground="#7c7c7c", relief=RAISED, borderwidth=1, command=programmeArrosage) #Programme d'arrosage
bp1()

b2 = Button(root, text="_", image=m, bg="#7c7c7c", activebackground="#7c7c7c", relief=RAISED, borderwidth=1, command=meteo) #Météo
bp2()

b3 = Button(root, text="_", image=th, bg="#7c7c7c", activebackground="#7c7c7c", relief=RAISED, borderwidth=1, command=tauxHumidite) #Taux d'humidité
bp3()

b4 = Button(root, text="_", image=re, bg="#7c7c7c", activebackground="#7c7c7c", relief=RAISED, borderwidth=1, command=reglages) #Réglages
bp4()

b5 = Button(root, text="_", image=ac, bg="#7c7c7c", activebackground="#7c7c7c", relief=RAISED, borderwidth=1, command=accueil) #Accueil
bp5()

b6 = Button(root, text="_", image=ve, bg="#7c7c7c", activebackground="#7c7c7c", relief=RAISED, borderwidth=1, command=veille) #Veille
bp6()

#BOOT GRAPH ACCUEIL-------------------------------------------------------------------------------------

imageAccueil = Label(root,text="_",borderwidth=0, bg="#404040", image=iea) #Image principale gicleur accueil

infoPA = Label(root,text="_",borderwidth=2) #Label milieu-bas Programme en cours

infoS = Label(root,text="_",borderwidth=0, bg="#404040", image=sIcone) #Icone secheresse

#BOOT ECRAN VEILLE--------------------------------------------------------------------------------------------

ecranVeille = Button(root, text="_", image=bgVeille, bg="black", activebackground="black", relief=FLAT, borderwidth=0, command=sortieVeille) #Ecran de Veille

#BOOT PAGE EN COURS (label)----------------------------------------------------------------------------------

pageEnCours = Label(root, text="_", borderwidth=0) #Boot de la fenêtre de page en cours

#BOOT SECHERESSE / ARRET SI PLUIE (ASP)

def check_SASP():
    global arrosageProgrammeActif, arrosageHumiditeActif, sArrosageProgrammeActif, sArrosageHumiditeActif, sdu
    while 1:
        with open("data/vSecheresse.txt","r") as vSecheresse:
            for line in vSecheresse.readlines():
                exec(line, globals())
        with open("data/vArrosageProgramme.txt","r") as vArrosageProgramme:
            for i in range(1):
                line=vArrosageProgramme.readline()
                exec(line, globals())
        with open("data/vArrosageHumidite.txt","r") as vArrosageHumidite:
            for i in range(1):
                line=vArrosageHumidite.readline()
                exec(line, globals())
        if secheresseActif==1 and sdu==0:
                sArrosageProgrammeActif=arrosageProgrammeActif
                sArrosageHumiditeActif=arrosageHumiditeActif
                arrosageProgrammeActif=0
                arrosageHumiditeActif=0
                if acceuilActif==1:
                    accueil()
                sdu=1
        if secheresseActif==0 and sdu==1:
            arrosageProgrammeActif=sArrosageProgrammeActif
            arrosageHumiditeActif=sArrosageHumiditeActif
            if acceuilActif==1:
                accueil()
            sdu=0
        ecrire_vSecheresse()
        ecrire_vArrosageProgramme()
        ecrire_vArrosageHumidite()
        time.sleep(5)

thread_time=threading.Thread(target=check_SASP)
thread_time.setDaemon(True)
thread_time.start()

#################################################################################################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################

#############  BOOT GRAPH  ###########################################################################################################################################################

#Boot graph zones

bZ1 = Button(root, text="_", image=iZ1, bg=None, activebackground=None, relief=FLAT, borderwidth=3, command=None) #Boot bouton graph zone 1
bZ2 = Button(root, text="_", image=iZ2, bg=None, activebackground=None, relief=FLAT, borderwidth=3, command=None) #Boot bouton graph zone 2
bZ3 = Button(root, text="_", image=iZ3, bg=None, activebackground=None, relief=FLAT, borderwidth=3, command=None) #Boot bouton graph zone 3
bZ4 = Button(root, text="_", image=iZ4, bg=None, activebackground=None, relief=FLAT, borderwidth=3, command=None) #Boot bouton graph zone 4
bZ5 = Button(root, text="_", image=iZ5, bg=None, activebackground=None, relief=FLAT, borderwidth=3, command=None) #Boot bouton graph zone 5

#Boot graph durée

lXMinutes = Label(root, image=xMinutes, bg="#b7b7b7", activebackground="#b7b7b7", relief=FLAT, borderwidth=0) #Boot fenêtre minutes dans choix de la durée
nombreDuree = Label(root, bg="#b7b7b7", relief=FLAT, borderwidth=0, fg="#ffffff") #Boot nombre de minutes dans choix de la durée

#Boot flêches (+/-/+10/-10)

bFlecheHaut = Button(root, image=flecheHaut, bg="#b7b7b7", activebackground="#b7b7b7", relief=None, borderwidth=1) #Boot fleche +
bP10Haut = Button(root, image=p10Haut, bg="#b7b7b7", activebackground="#b7b7b7", relief=None, borderwidth=1) #Boot fleche +10
bP10Bas = Button(root, image=p10Bas, bg="#b7b7b7", activebackground="#b7b7b7", relief=None, borderwidth=1) #Boot fleche -
bFlecheBas = Button(root, image=flecheBas, bg="#b7b7b7", activebackground="#b7b7b7", relief=None, borderwidth=1) #Boot fleche -10

#Boot graph horaire

lXHoraire = Label(root, image=xHoraire, bg="#b7b7b7", activebackground="#b7b7b7", relief=FLAT, borderwidth=0) #Boot fenêtre h / min dans choix de l'horaire
bSHeure = Button(root, image=selectHeure, bg="#b7b7b7", activebackground="#b7b7b7", relief=None, borderwidth=1, command=hHeure) #Boot bouton selection des heures
bSMinutes = Button(root, image=selectMinutes, bg="#b7b7b7", activebackground="#b7b7b7", relief=None, borderwidth=1, command=hMinutes) #Boot bouton selection des minutes
hH = Label(root, text=nH, bg="#b7b7b7", relief=FLAT, borderwidth=0, fg="#ffffff", font=policeHH) #Boot nombre d'heures dans choix de l'horaire
hM = Label(root, text=nM, bg="#b7b7b7", relief=FLAT, borderwidth=0, fg="#ffffff", font=policeHM) #Boot nombre de minutes dans choix de l'horaire

#Boot graph Taux humidite

lTH1=Label(root, image=TH1, bg="#b7b7b7", activebackground="#b7b7b7", relief=FLAT, borderwidth=0) #Boot cases taux humidite
lTH2=Label(root, image=TH2, bg="#b7b7b7", activebackground="#b7b7b7", relief=FLAT, borderwidth=0)
lTH3=Label(root, image=TH3, bg="#b7b7b7", activebackground="#b7b7b7", relief=FLAT, borderwidth=0)
lTH4=Label(root, image=TH4, bg="#b7b7b7", activebackground="#b7b7b7", relief=FLAT, borderwidth=0)
lTH5=Label(root, image=TH5, bg="#b7b7b7", activebackground="#b7b7b7", relief=FLAT, borderwidth=0)

for i in range(0,5):
    lTH100[i]=Label(root, image=TH100, relief=FLAT, borderwidth=0) #Boot gouttes 100
for i in range(0,5):
    lTH75[i]=Label(root, image=TH75, relief=FLAT, borderwidth=0) #Boot gouttes 75
for i in range(0,5):
    lTH50[i]=Label(root, image=TH50, relief=FLAT, borderwidth=0) #Boot gouttes 50
for i in range(0,5):
    lTH25[i]=Label(root, image=TH25, relief=FLAT, borderwidth=0) #Boot gouttes 25
for i in range(0,5):
    lPTH[i]=Label(root, text=nPTH[i], font=policeTH, bg="#afafaf", activebackground="#afafaf", fg="#ffffff") #Boot label taux humidite

#Boot graph Meteo

lMTime=Label(root, image=mHeure, relief=FLAT, borderwidth=0)
lTime=Label(root, text="", bg="#b7b7b7", relief=FLAT, borderwidth=0, fg="#ffffff", font=policeM1)
lMTemp=Label(root, image=mTemperature, relief=FLAT, borderwidth=0)
lTemp=Label(root, text="", bg="#b7b7b7", relief=FLAT, borderwidth=0, fg="#ffffff", font=policeM1)
lMTMax=Label(root, image=mTMax, relief=FLAT, borderwidth=0)
lTMax=Label(root, text="", bg="#b7b7b7", relief=FLAT, borderwidth=0, fg="#ff7171", font=policeM2)
lMTMin=Label(root, image=mTMin, relief=FLAT, borderwidth=0)
lTMin=Label(root, text="", bg="#b7b7b7", relief=FLAT, borderwidth=0, fg="#5895c4", font=policeM2)
lMCond=Label(root, image=None, relief=FLAT, borderwidth=0)

thread_time=threading.Thread(target=timeAct)
thread_time.setDaemon(True)
thread_time.start()

#Boot graph DescZones

lIDZ=Label(root, image=iDZ, bg="#b7b7b7", activebackground="#b7b7b7", relief=FLAT, borderwidth=0)
lWarnClavier=Label(root, image=warnClavier, bg="#b7b7b7", activebackground="#b7b7b7", relief=FLAT, borderwidth=0)
bEdit=Button(root, image=warnClavier, bg="#b7b7b7", activebackground="#b7b7b7", command=editDZ)
for i in range(0,5):
    eDZ[i] = Entry(root, bg="#e6e6e6", bd=0, fg="black", disabledforeground="black", disabledbackground="#e6e6e6", justify=LEFT, state=NORMAL, width=26, font=policeDZ, textvariable=sEDZ[i])

#Boot graph imagesCentrales

lImageAide = Label(root, image=imageAide, relief=FLAT, bd=0)
lImageManuel = Label(root, image=imageManuel, relief=FLAT, bd=0)
lImageProgramme = Label(root, image=imageProgramme, relief=FLAT, bd=0)
lImageHumidite = Label(root, image=imageHumidite, relief=FLAT, bd=0)
lMpm = Label(root, image=mpm, relief=FLAT, bd=0)
lSelectZoneSVP = Label(root, image=selectZoneSVP, relief=FLAT, bd=0)
lImageReglages = Label(root, image=imageReglages, relief=FLAT, bd=0)

#################################################################################################################################################################################
#################################################################################################################################################################################


#LANCEMENT--------------------------------------------------------------------------------------------------------

accueil() #Fin de l'initialisation, lancement de l'application

################################################################################################################################################################################

root.mainloop()