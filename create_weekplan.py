from lebensmittel_db import lebensmittel_db
from random import choice

class Mahlzeit:
    def __init__(self, name, zutaten):
        self.name = name
        self.zutaten = zutaten

def wochenplan_erstellen(kcal_pro_tag=1600, protein_prozent=33, kohlenhydrate_prozent=47, fett_prozent=20,
                         fruehstueck_options=[], mittagessen_options=[], snack_options=[], abendessen_options=[]):

    # Kalorien für Protein, Fette und Kohlenhydrate berechnen
    protein_kcal = (protein_prozent / 100) * kcal_pro_tag
    fett_kcal = (fett_prozent / 100) * kcal_pro_tag
    kohlenhydrate_kcal = (kohlenhydrate_prozent / 100) * kcal_pro_tag

    # Zufällige Auswahl von Lebensmitteln aus den Lebensmitteloptionen
    def zufaellige_lebensmittel(optionen):
        zutaten = []
        for option in optionen:
            lebensmittel = choice(option)
            zutaten.append(lebensmittel)
            # Makronährstoffverteilung für jedes Lebensmittel berücksichtigen
            protein_kcal -= lebensmittel_db[lebensmittel]["Protein"]
            fett_kcal -= lebensmittel_db[lebensmittel]["Fett"]
            kohlenhydrate_kcal -= lebensmittel_db[lebensmittel]["Kohlenhydrate"]
        return zutaten

    mahlzeiten = [
        Mahlzeit("Frühstück", zufaellige_lebensmittel(fruehstueck_options)),
        Mahlzeit("Mittagessen", zufaellige_lebensmittel(mittagessen_options)),
        Mahlzeit("Snack", zufaellige_lebensmittel(snack_options)),
        Mahlzeit("Abendessen", zufaellige_lebensmittel(abendessen_options))
    ]

    # Wochenplan ausgeben
    print("Wochenplan:")
    for mahlzeit in mahlzeiten:
        print(f"{mahlzeit.name}: {', '.join(mahlzeit.zutaten)}")

# Beispielaufruf mit personalisierten Gerichtoptionen
fruehstueck_options = [["Hähnchen", "Thunfisch", "Ei"], ["Tofu", "Lachs", "Ei"]]
mittagessen_options = [["Tofu", "Thunfisch"], ["Hähnchen", "Lachs"], ["Thunfisch", "Ei"]]
snack_options = [["Nüsse", "Ei"], ["Thunfisch", "Tofu"], ["Hähnchen", "Ei"]]
abendessen_options = [["Tofu", "Lachs", "Thunfisch"], ["Hähnchen", "Ei"], ["Lachs", "Ei"]]

wochenplan_erstellen(fruehstueck_options=fruehstueck_options,
                     mittagessen_options=mittagessen_options,
                     snack_options=snack_options,
                     abendessen_options=abendessen_options)
