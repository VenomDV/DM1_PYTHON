print ("Bienvenue au restaurant PyFood\n")
print ("Les entrées :")
print ("1- Salade de chef . . . . . . . . 12 €") 
print ("2- Salade niçoise . . . . . . . . 10 €")
print ("3- Salade grecque . . . . . . . . 9 €")
print ("4- Salade italienne . . . . . . . 11 €\n")

Echoix_str = input ("Choisir votre entrée : ")
print ("\n")

try:
    Echoix_int = int(Echoix_str) 
except:
     print ("Saisissez une valeur numerique !!\n")    
else:
    while Echoix_int < 1 or Echoix_int > 4:
        print ("Les entrées :")
        print ("1- Salade de chef . . . . . . . . 12 €") 
        print ("2- Salade niçoise . . . . . . . . 10 €")
        print ("3- Salade grecque . . . . . . . . 9 €")
        print ("4- Salade italienne . . . . . . . 11 €\n")
        Echoix_int = int (input ("Veuillez choisir une des entrées qui vous es proposé :"))
    if (Echoix_int == 1):
        print ("Vous avez choisi: La salade de chef.\n")
        prix_entree = 12
    elif (Echoix_int == 2):
        print ("Vous avez choisi: La salade niçoise.\n")
        prix_entree = 10
    elif (Echoix_int == 3):
        print ("Vous avez choisi: La salade grecque.\n")
        prix_entree = 9
    elif (Echoix_int == 4):
        print ("Vous avez choisi: La salade italienne.\n")
        prix_entree = 11

print ("Les plats :")
print ("1- Fritures de poissons . . . . . .25 €")
print ("2- Bavette de voeu . . . . . . . . 19 €")
print ("3- Saumon a la plancha . . . . . . 22 €")
print ("4- Boeuf bourguigons . . . . . . . 16 €\n")

Pchoix_str = input ("Choisir votre plat : ")
print ("\n")

try:
    Pchoix_int = int (Pchoix_str)
except: 
    print ("Saisissez une valeur numerique !!\n")
else:
    while Pchoix_int < 1 or Pchoix_int > 4:
        print ("Les plats :")
        print ("1- Fritures de poissons . . . . . .25 €")
        print ("2- Bavette de voeu . . . . . . . . 19 €")
        print ("3- Saumon a la plancha . . . . . . 22 €")
        print ("4- Boeuf bourguigons . . . . . . . 16 €\n")
        Pchoix_int = int(input("Veuillez choisir un des plats qui vous es proposé :"))
    if (Pchoix_int == 1):
        print ("Vous avez choisi: La Fritures de poissons.\n")
        prix_plat = 25
    elif (Pchoix_int == 2):
        print ("Vous avez choisi: La Bavette de voeu.\n")
        prix_plat = 19
    elif (Pchoix_int == 3):
         print ("Vous avez choisi: Le Saumon a la plancha.\n")
         prix_plat = 22
    elif (Pchoix_int == 4):
         print ("Vous avez choisi: Le Boeuf bourguigons.\n")
         prix_plat = 16

print ("Les desserts:")
print ("1- Creme brulee . . . . . . . . . . 7 €")
print ("2- Tiramissu . . . . . . . . . . . .8 €")
print ("3- Glace au choix . . . . . . . . . 9 €")
print ("4- Panacota . . . . . . . . . . . . 6 €\n")

Dchoix_str = input ("Choisir votre dessert : ")
print ("\n")

try:
    Dchoix_int = int (Dchoix_str)
except:
    print ("Saisissez une valeur numerique !!\n")
else:
    while Dchoix_int < 1 or Dchoix_int > 4:
        print ("Les desserts :")
        print ("1- Creme brulee . . . . . . . . . . 7 €")
        print ("2- Tiramissu . . . . . . . . . . . .8 €")
        print ("3- Glace au choix . . . . . . . . . 9 €")
        print ("4- Panacota . . . . . . . . . . . . 6 €\n")
        Dchoix_int = int (input ("Veuillez choisir un des désserts qui vous es proposé :"))
    if (Dchoix_int == 1):
        print ("Vous avez choisi: La Creme brulee.\n")
        prix_dessert = 7
    elif (Dchoix_int == 2):
        print ("Vous avez choisi: Le Tiramissu.\n")
        prix_dessert = 8
    elif (Dchoix_int == 3):
        print ("Vous avez choisi: La Glace au choix.\n")
        prix_dessert = 9
    elif (Dchoix_int == 4):
        print ("Vous avez choisi: La Panacota.\n")
        prix_dessert = 6

print (f"Total à payer : {prix_entree} € + {prix_plat} € + {prix_dessert} € = {prix_entree + prix_plat + prix_dessert} €\n")