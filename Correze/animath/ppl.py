# %%
import unicodedata


def strip_accents(s: str) -> str:
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


# %%
prologin_finalistes = """Guillaume Bertholo
Quentin Juppet
Marc Dufay
Félix Breton
Yoann Coudert-Os
Timothée Darcet
Victor Deng
Alban Reynaud
Hugo Peyraud-Mag
Olivér Facklam
Ernest Van Wijland
Oscar Boutin
Noël Nadal
Victor Dheur
Marc Pierre
Jean Jouve
Théophane Vallaey
Hugues Déprés
Nicolas Vallée
Corentin Simon
Arthur Migliorini
Flavien Solt
Théo Lenoir
Paul Du
Rémy Kimbrough
Erwin Deng
Benjamin Peyrille
Hippolyte Muziot
Damien Girault
Baptiste Jacquem
Julien Weibel
Thomas Agugliaro
Nicolas Daire
Quentin Le Meur
Noé Weeks
Ronan Pelliard
Robin Jadoul
Gabrielle Pauvert
Adrien Vannson
Sylvain Vaure
Octave Hazard
Paul Le Grand Des Cloizeaux
Noémie Jacquemo
Damien Galant
Nicolas Gues
Eloi Démolis
Nicolas Buton
Nathan Kessler
Arnaud Lequen
David Robin
Victor Amblard
Malo Jaffré
Jingjie Yang
Thibauld Feneuil
Jean-Marie Mineau
Elias Suvanto
Ilyas Lebleu
Moana Jubert
Bastien Mignoty
Paul-Adrien Nicole
Lucas Lefebvre-Ler
Emile Hohnadel
Maël Saillot
Adrien Rospars
Baptiste Collet
Victor Miquel
Mourtaza Abbasbh
Philippe Anjolras
Claire Soyez-Marti
Killian Dengreville
Gwénaëlle Bienven
Matthias Rigaud
Wagner Rodrigues
Baptiste Tesson
Simon Dupouy
Amadeus Reinald
Esteban Christiann
Guillaume Bernos
Guillaume Augusto
Alain Delaet
Joseph Priou
Colin Davalo
Jules Bertrand
Elodie Bernard
Hugo Jacob
Maxime Benrubi
Pierre Le Scornet
Quentin Buzet
Pablo Destic
Louis Cousturian""".split('\n')
prologin_ = []
for name in prologin_finalistes:
    first, *last = name.split(' ')
    prologin_.append(strip_accents(f"{' '.join(last)} {first}".upper()))
prologin_finalistes = prologin_

# %%
animaths_summer_camp = """Averous,Emile
Peeters,Marie
Gay,Sylvain
Léonard,Arthur
Narozniak,Gaëtan
Pigé,Xavier
Hamimed,Adam
Zablocki,Jean
HUA,Lucien
ROCQUET,Timothée
Rossignol,Etienne
Shirazi,Madison
Bouyer,Matthieu
CHAPOT,Clément
CHEN,Michaël
Fougereux,Théodore
Ringeard,Timothé
DUPLESSIS,Alexandre
de Lambilly,Auguste
Finocchiaro,Leonardo
De Montgolfier,Nathan
Rosaz,Paul
Jimenez Calles,Gabriel
Pétry,Enora
Vassaux,Louis
VINCENT,Pierrick
Artru,Noé
Audusse,Elio
Wetterwald,Mathis
Kittel,Léonie
Gueugneau,Pierre
Popescu,Andrei
Vantalon,gautier
CHABREDIER,Sylvain
Barbu,Andrei
Caillot,Alexandre
Legros,Aymeric
LENORMAND,JOSEPH
Ayanides,Pierre
Yang,Jingjie""".split('\n')
animaths_summer_camp = [
    strip_accents(name.replace(',', ' ').upper())
    for name in animaths_summer_camp
]

# %%
kang_top_100 = """AYANIDES PIERRE
SHIRAZI MADISON
BALLIF PIERRE
YANG JINGJIE
POYET ROMAIN
ZABLOCKI JEAN
DIKICI DOGA DENIZ
DAI LINKAI
GAY SYLVAIN
DUPLESSIS ALEXANDR
KOCKAR BERNA
LLORIN AMAURY
TERNOT MAXIME
TUNCER DURU
TERNOT BENJAMIN
MOLFESSIS THEO
GILLOT EDERN
DELOIRE NATHAN
NAROZNIAK GAETAN
ORTCHEMSKI ALEXAN
JANICOT PAUL
PERE DEODAT
DURAND CYPRIEN
BERGER JONAS
LENORMAND JOSEPH
ROQUES TIMOTHEE
VIATTE ELEONORE
LECOINTRE PAUL
GOGUET MARIUS
LODAY YOANN
SONG DORIAN
SURUCU ATILA
UTHURRIAGUE ELISA
JEROME NASR
CALISKAN BEYZA
DORSEEIL VALENTIN
HAN BRYAN
DEHAIS NICOLAS
AHN CHANGYON
BUCAILLE VLADIMIR
DUCLERT ALEXIA
TATON MATHIS
ROSAZ PAUL
ONCU RUMEYSA
BURKHARDT LEON
GERODOU THOMAS
BERANGER SOPHIE
ORNEK RUMET
MONTOYA SAMUEL
PAPON THOMAS
NOVAT THIBAULT
UNLU SELEN
RONG CLAIRE
BOUAT ALEXANDRE
VINDRY GUILLAUME
MEIER THEO
ELMAS KEREM
WEHRUNG JONAS
ANTOINE ARTHUR
DEGRYSE MATHIS
VANBORRE PAUL
MONTOYA YANN
EISSELBERGER TIMO
COLLIGNON MAXIME
LEESCO LEO
JACQUIN PIERRE
BLANPAIN VALENTINE
LE MARECHAL PRUNE
DEMIR IKBAL SENA
ATES MELIS
LABELLE JULIE
BULTEAU BARTHELEM
TASYUREK EKIN
CHEFTEL NICOLAS
AYDIN ZEYNEP
LEGUEDART LENAIC
HOFF MATHIEU
POPESCU ANDREI
CLESCA DEDIEU VANIA
LEFEVRE ANNABELLE
BRIAND VICTOR
CAILLOT ALEXANDRE
MERILLON NATHAN
IZORET ANTHONIN
BOSTANCI BERKAN
KAHIGAN DERYA
CLEVELAND ELECTA
HAMZAOUI AMIN
LEQUIN VICTOR
SAUBOT ARTHUR
HEITZ CHARLES
SENAY ILAY ZEHRA
ILTER GOKTUG
OMARIE OLIVIER
DANIS DILBA
BARRAQUE PAUL
BERDUGO BLANDINE
RICHARD ELIAN
TARK SEHYUN
EMERDJIAN THOMAS""".split('\n')

# %%
set(prologin_finalistes) & set(animaths_summer_camp)

# %%
set(prologin_finalistes) & set(kang_top_100)

# %%
set(kang_top_100) & set(animaths_summer_camp)
