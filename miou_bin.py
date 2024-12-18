#list_mot = ["miaou","meow"]

lettre_min = "abcdefghijklmnopqrstuvwxyz"
lettre_maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
maj_vers_min = {lettre_maj[i]: lettre_min[i] for i in range(26)}
min_vers_maj = {lettre_min[i]: lettre_maj[i] for i in range(26)}

dictio_car_bin = {
    "miaou":{
    " ": 0,
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9, 
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18, 
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    ".": 27,
    "!": 28,
    "?": 29,
    ",": 30,
    ";": 31,
    },
    "grrr":{
    "0":0,
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "+":10,
    "-":11,
    "*":12,
    "/":13,
    "=":14,
    "%":15,
    },
    "meow":{
        "<":0,
        ">":1,
        "(":2,
        ")":3,
        "[":4,
        "]":5,
        "{":6,
        "}":7,
        "#":8,
        "@":9,
        "&":10,
        "|":11,
        "$":12,
        "€":13,
        "£":14,
        "¥":15,
    }
}
dictio_car_bin_inv={mot:{v:k for k,v in dictio_car_bin[mot].items()} for mot in dictio_car_bin.keys()}

#256,128,64,32,16,8,4,2,1   

def converti_int_vers_bin(nb:int,taille:int) -> str:
    sortie=""
    for _ in range(taille):
        sortie =str(nb%2) + sortie
        nb = nb//2
    return sortie

def converti_bin_vers_int(bin:str) -> int:
    sortie = 0
    for i in range(len(bin)):
        sortie += int(bin[i])*(2**(len(bin)-1-i))
    return sortie

def converti_lettre_vers_bin(lettre :str,mot:str) -> str:
    return converti_int_vers_bin(dictio_car_bin[mot][lettre],len(mot))

def converti_bin_vers_lettre(bin:str,mot:str) -> str:
    entier=converti_bin_vers_int(bin)
    return dictio_car_bin_inv[mot][entier]

def converti_lettre_vers_motbin(lettre:str,mot:str) -> str:
    bin=converti_lettre_vers_bin(lettre,mot)
    mot_bin=""
    for i in range(len(bin)):
        if bin[i] == "1":
            mot_bin += mot[i].upper()
        else:
            mot_bin += mot[i]
    return mot_bin

def converti_motbin_vers_lettre(mot_bin:str) -> str:
    if len(mot_bin) == 0:
        return ""
    bin=""
    for i in range(len(mot_bin)):
        if mot_bin[i] == mot_bin[i].upper():
            bin += "1"
        else:
            bin += "0"
    return converti_bin_vers_lettre(bin,mot_bin.lower())

def trouve_mot_pour_lettre(lettre:str) -> str:
    for mot in dictio_car_bin.keys():
        if lettre in dictio_car_bin[mot].keys():
            return mot
    return ""

def converti_texte_vers_miou(texte:str) -> str:
    sortie=""
    for lettre in texte:
        lettre = lettre.lower()
        mot = trouve_mot_pour_lettre(lettre)
        if len(mot) == 0:
            print("Erreur : lettre non trouvée ("+lettre+")")
        else:
            sortie += converti_lettre_vers_motbin(lettre,mot) + " "
    return sortie

def converti_miou_vers_texte(miou:str) -> str:
    sortie=""
    list_miou = miou.split(" ")
    for mot_bin in list_miou:
        sortie += converti_motbin_vers_lettre(mot_bin)
    return sortie

def mioleur(texte:str) -> str:
    """Traduit un texte normal en texte miou"""
    return converti_texte_vers_miou(texte)

def traducteur(miou:str) -> str:
    """Traduit un texte miou en texte normal"""
    return converti_miou_vers_texte(miou)

def main():
    texte = "blabla"
    miou = mioleur(texte)
    print(miou)
    texte = traducteur(miou)
    print(texte)

if __name__ == "__main__":
    main()