#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'covid19Analiza.py'
__version__ = '0.1'
__site__ = 'pythonbytes.rs'

import sys
from subprocess import call

try:
    import pandas as pd
    import matplotlib.pyplot as plt
    from colorama import Fore
except:
    call('pip3 install colorama pandas matplotlib', shell=True)
    exit()


def logo():
    print(Fore.RED+"\n       __           __        ____      __        ")
    print(Fore.RED+"  ____/ /___ ______/ /_______/ __ \____/ /__  _____ ")
    print(Fore.RED+" / __  / __ `/ ___/ //_/ ___/ / / / __  / _ \/ ___/ ")
    print(Fore.RED+"/ /_/ / /_/ / /  / ,< / /__/ /_/ / /_/ /  __/ /     ")
    print(Fore.RED+"\__,_/\__,_/_/  /_/|_|\___/\____/\__,_/\___/_/      ")
    print(Fore.RED+"                                                \n")
    print(Fore.RED+'                               Naziv: '+ __scriptName__)
    print(Fore.RED+'                               Verzija: '+ __version__)
    print(Fore.RED+'                               Koder: '+ __coder__)
    print(Fore.RED+ '                               Sajt: ' + __site__+Fore.WHITE)

if sys.platform == 'linux' or sys.platform == 'linux2' or sys.platform == 'darwin':
    call('clear', shell=True)
    logo()
else:
    call('cls', shell=True)
    logo()

def covid19(DRZAVE):
    plt.figure('COVID-19 - Pozitivni u okruzenju') # Naziv prozora
    AX = plt.subplot(111)
    AX.set_facecolor('#121212') # Boja pozadine gde je dijagram
    AX.figure.set_facecolor('black') # Boja pozadine
    AX.tick_params(axis='x', colors='red') # Boja brojeva na x osi
    AX.tick_params(axis='y', colors='red') # Boja brojeva na y osi
    AX.set_title('COVID-19 - Ukupan broj pozitivnih', color='red') # Title prikaza

    for drzava in DRZAVE:
        POTVRDJENI[drzava].plot(label=drzava)

    plt.legend(loc='upper left') # Mesto gde su upisane drzave (gornji levi ugao, nema logike da bude u desnom)
    plt.show()

if __name__ == '__main__':
    print('\n[+] Dobrodosli u skriptu koja prikazuje ukupan broj pozitivnih na COV-19 u okruzenju.')
    POTVRDJENI = pd.read_csv('potvrdjeni.csv') # Ucitati csv fajl
    UMRLI = pd.read_csv('umrli.csv') # Ucitati csv fajl
    OPORAVLJENI = pd.read_csv('oporavljeni.csv') # Ucitati csv fajl

    POTVRDJENI = POTVRDJENI.drop(['Province/State', 'Lat', 'Long'], axis=1) # Skloniti ove kolone
    UMRLI = UMRLI.drop(['Province/State', 'Lat', 'Long'], axis=1) # Skloniti ove kolone
    OPORAVLJENI = OPORAVLJENI.drop(['Province/State', 'Lat', 'Long'], axis=1) # Skloniti ove kolone

    POTVRDJENI = POTVRDJENI.groupby(POTVRDJENI['Country/Region']).aggregate('sum') # Sabrati sve redove u jedan red. Posto pojedine zemlje imaju vise redova
    UMRLI = UMRLI.groupby(UMRLI['Country/Region']).aggregate('sum') # Sabrati sve redove u jedan red. Posto pojedine zemlje imaju vise redova
    OPORAVLJENI = OPORAVLJENI.groupby(OPORAVLJENI['Country/Region']).aggregate('sum') # Sabrati sve redove u jedan red. Posto pojedine zemlje imaju vise redova

    POTVRDJENI = POTVRDJENI.T # Transpose index i kolone. Preko glavne dijagonale upisuje redove i kolone i obrnuto.
    UMRLI = UMRLI.T
    PORAVLJENI = OPORAVLJENI.T

    DRZAVE = ['Serbia', 'Bosnia and Herzegovina', 'Montenegro', 'Croatia', 'Albania', 'Hungary', 'Romania', 'Bulgaria'] # Drzave koje zelimo da prikazemo
    covid19(DRZAVE)







