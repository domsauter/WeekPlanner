from random import uniform, choice
from lebensmittel_db import lebensmittel_db

def zufaellige_lebensmittel(optionen, kalorien_rest):
    zutaten = []
    
    for kategorie in optionen:
        lebensmittel = choice(list(lebensmittel_db[kategorie].keys()))
        kalorien_pro_100g = lebensmittel_db[kategorie][lebensmittel]["Kalorien"]
        
        # Berechnung der maximalen Grammzahl basierend auf verbleibenden Kalorien und einer realistischen Obergrenze
        max_gramm = min(kalorien_rest / kalorien_pro_100g * 100, 300)  # Maximal 300g pro Mahlzeit
        
        # Runden der Grammzahl auf eine Dezimalstelle
        gramm = round(uniform(50, max_gramm), 1)
        
        # Sicherstellen, dass Gramm nicht negativ wird
        if gramm < 0:
            gramm = 0
        
        # Hinzufügen des ausgewählten Lebensmittels zur Zutatenliste
        zutaten.append((lebensmittel, gramm, kategorie))
        
        # Aktualisieren der verbleibenden Kalorien
        kalorien_rest -= kalorien_pro_100g * (gramm / 100)
    
    return zutaten, kalorien_rest

def wochenplan_erstellen(kcal_pro_tag=1600, protein_prozent=33, kohlenhydrate_prozent=47, fett_prozent=20,
                         fruehstueck_options=[], mittagessen_options=[], snack_options=[], abendessen_options=[]):
    
    # Berechnung der Kalorien für Protein, Fette und Kohlenhydrate
    protein_kcal = (protein_prozent / 100) * kcal_pro_tag
    fett_kcal = (fett_prozent / 100) * kcal_pro_tag
    kohlenhydrate_kcal = (kohlenhydrate_prozent / 100) * kcal_pro_tag
    
    # Kalorienaufteilung für jede Mahlzeit
    fruehstueck_kalorien = 0.2 * kcal_pro_tag
    mittagessen_kalorien = 0.35 * kcal_pro_tag
    snack_kalorien = 0.1 * kcal_pro_tag
    abendessen_kalorien = 0.35 * kcal_pro_tag
    
    # Erstellen der Mahlzeiten
    mahlzeiten = []
    
    # Frühstück
    zutaten, fruehstueck_kalorien = zufaellige_lebensmittel(fruehstueck_options, fruehstueck_kalorien)
    mahlzeiten.append({
        "name": "Frühstück",
        "zutaten": zutaten,
        "kalorien": round(fruehstueck_kalorien, 2)  # Runden auf zwei Dezimalstellen
    })
    
    # Mittagessen
    zutaten, mittagessen_kalorien = zufaellige_lebensmittel(mittagessen_options, mittagessen_kalorien)
    mahlzeiten.append({
        "name": "Mittagessen",
        "zutaten": zutaten,
        "kalorien": round(mittagessen_kalorien, 2)  # Runden auf zwei Dezimalstellen
    })
    
    # Snack
    zutaten, snack_kalorien = zufaellige_lebensmittel(snack_options, snack_kalorien)
    mahlzeiten.append({
        "name": "Snack",
        "zutaten": zutaten,
        "kalorien": round(snack_kalorien, 2)  # Runden auf zwei Dezimalstellen
    })
    
    # Abendessen
    zutaten, abendessen_kalorien = zufaellige_lebensmittel(abendessen_options, abendessen_kalorien)
    mahlzeiten.append({
        "name": "Abendessen",
        "zutaten": zutaten,
        "kalorien": round(abendessen_kalorien, 2)  # Runden auf zwei Dezimalstellen
    })
    
    # Ausgabe des Wochenplans
    print("Wochenplan:")
    for mahlzeit in mahlzeiten:
        print(f"{mahlzeit['name']}:")
        for zutat in mahlzeit['zutaten']:
            print(f"  {zutat[0]} ({zutat[2]}), {zutat[1]}g")
        print(f"  Kalorien: {mahlzeit['kalorien']} kcal")
        print()

# Beispielaufruf mit personalisierten Gerichtoptionen
fruehstueck_options = ["Protein", "Kohlenhydrate", "Fett"]
mittagessen_options = ["Protein", "Kohlenhydrate", "Fett", "Gemüse"]
snack_options = ["Protein", "Kohlenhydrate", "Fett", "Gemüse"]
abendessen_options = ["Protein", "Kohlenhydrate", "Fett", "Gemüse"]

wochenplan_erstellen(fruehstueck_options=fruehstueck_options,
                     mittagessen_options=mittagessen_options,
                     snack_options=snack_options,
                     abendessen_options=abendessen_options)
