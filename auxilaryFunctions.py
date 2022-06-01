import pandas as pd
import matplotlib.pyplot as plt

def podaci_po_godinama(df):
    godine = []
    izaslo = []
    prijavilo = []
    for godina in df['skolska_godina_roka'].unique():
        godina_df = df[df['skolska_godina_roka'] == godina]
        godine.append(godina)
        izaslo.append(sum(godina_df['ukupno_prijavilo']))
        prijavilo.append(sum(godina_df['ukupno_izaslo']))
    return godine, izaslo, prijavilo

def podaci_po_mesecima(df):
    meseci = ['јануар', 'фебруар', 'јун', 'јул','август', 'септембар', 'октобар']
    godine = []
    izaslo = []
    prijavilo = []
    for mesec in meseci:
        godina_df = df[df['tip_roka'] == mesec]
        godine.append(mesec)
        izaslo.append(sum(godina_df['ukupno_prijavilo']))
        prijavilo.append(sum(godina_df['ukupno_izaslo']))
    return godine, izaslo, prijavilo

def custom_plot(labels, data, title="",  ylabel="", xlabel="", name=""):
    ticks = range(len(labels))
    plt.figure(tight_layout=True)
    plt.xticks(ticks, labels)
    plt.plot(data, 'o-', linewidth=2)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.grid()
    plt.savefig('Grafici/'+name+'_grafik.png')