import sys
from pathlib import Path
from perception import *
from memoire import *

import reconfort_io as rio

def main(argv):
    if len(argv) != 5:
        print(__doc__.strip())
        return 2

    chemin_carte, chemin_scenario = Path(argv[1]), Path(argv[2])
    dossier_donnees, chemin_sortie = Path(argv[3]), Path(argv[4])

    try:
        carte = rio.charger_carte(chemin_carte)
        scenario = rio.charger_scenario(chemin_scenario)
        dictionnaire = rio.charger_dictionnaire(
            dossier_donnees / "dictionnaire.json")
        armoire = rio.charger_armoire(
            dossier_donnees / f"{scenario['armoire']}.json")
    except rio.ErreurFichier as err:
        print(f"erreur de chargement : {err}", file=sys.stderr)
        return 1

    print(f"carte        : {carte['nom']} "
          f"{carte['dimensions']['hauteur']}x{carte['dimensions']['largeur']}, "
          f"{len(carte['residents'])} residents")
    print(f"scenario     : {scenario['nom']}, "
          f"{len(scenario['demandes'])} demandes")
    print(f"dictionnaire : {len(dictionnaire['entrees'])} entrees")
    print(f"armoire      : {armoire['nom']}, "
          f"{len(armoire['casiers'])} casiers")
    print()

    # Ce que voit le robot au depart : sa position, celle de l'armoire, celle
    # du dictionnaire, et celles des residents. Les murs, eux, ne sont PAS
    # connus a priori, et le contenu des casiers non plus (enonce 3.2 et 3.3).
    # Ne lisez ni carte["grille"], ni le champ "objet" des casiers : votre
    # agent n'y a pas droit.
    print(f"depart robot   : {carte['depart_robot']}")
    print(f"armoire        : {carte['armoire']['position']}")
    print(f"dictionnaire   : {carte['dictionnaire']['position']}")
    print(f"casier depart  : {armoire['casier_depart']}")
    print(f"legende: {carte['legende']}")

    caseN, caseS, caseE, caseO = see(carte['grille'], carte['depart_robot'])
    print(f"case N: {caseN}")
    print(f"case S: {caseS}")
    print(f"case E: {caseE}")
    print(f"case O: {caseO}")


    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))