solar = {}
def adauga_echipament(id, tip, nume, stare, parametrii):
    solar[id] = {
        "tip" : tip,
        "nume" : nume,
        "stare" : stare,
        "parametrii": parametrii,
    }

def listare_echipamente():
    print("---ECHIPAMENTE SOLAR---")
    for id_echipament in solar:
        echipament = solar[id_echipament]
        print(
            f"ID:{id_echipament} \n Denumire:{echipament['nume']} \n Tip:{echipament['tip']} \n Stare:{echipament['stare']}"
        )
        print(f" Parametrii:{echipament['parametrii']} \n")

def comanda(id_echipament, tip_comanda, stare, valoare=None):
    
    if id_echipament not in solar:
        print(f"EROARE; Echipamentul {id_echipament} nu exista")
        return

    echipament = solar[id_echipament]

    if tip_comanda == "stare":
        echipament["stare"] = stare
        print(f"{id_echipament}: starea a fost schimbata in '{stare}'")
    elif tip_comanda == "parametru":
        echipament["parametrii"][stare] = valoare
        print(f"{id_echipament}: parametrul a fost schimbat in '{valoare}'")

def citire_stare(id_echipament):
    if id_echipament not in solar:
        print(f"EROARE; Echipamentul {id_echipament} nu exista")
        return
    
    echipament=solar[id_echipament]
    print(f"Starea echipamentului '{id_echipament}' este: {echipament['stare']}")

def agregare():
    nr=0
    stari=0
    for id_echipament in solar:
        echipament = solar[id_echipament]
        nr+=1
        if(echipament['stare'] in ["pornit", "activ", "deschis"]):
            stari+=1
    print(f"Sunt {nr} echipamente in total si {stari} sunt pe modul pornit")

adauga_echipament("PMP-1", "pompa", "Pompa_Picurare", "oprit", {"debit_l_min": 10})
adauga_echipament("SNZR-1", "senzor", "Senzor_clima", "pornit", {"temperatura_c": 26.5, "umiditate": 75})
adauga_echipament("AER-1","aerisire", "Trapa-Nord", "deschis", {"procent_deschidere": 40})
listare_echipamente()
comanda("PMP-1", "parametru", "debit_l_min", 25)
comanda("SNZR-1", "stare", "oprit")
listare_echipamente()
citire_stare("PMP-1")
citire_stare("SNZR-1")
agregare()