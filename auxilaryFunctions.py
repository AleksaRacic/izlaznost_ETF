import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

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
    meseci_ = ['јануар', 'фебруар', 'јун', 'јул','август', 'септембар', 'октобар']
    meseci = []
    izaslo = []
    prijavilo = []
    for mesec in meseci_:
        godina_df = df[df['tip_roka'] == mesec]
        meseci.append(mesec)
        izaslo.append(sum(godina_df['ukupno_prijavilo']))
        prijavilo.append(sum(godina_df['ukupno_izaslo']))
    return meseci, izaslo, prijavilo

def po_godinama_mesecima(df):
    meseci_ = ['јануар', 'фебруар', 'јун', 'јул','август', 'септембар', 'октобар']
    po_godinama = {}
    for godina in df['skolska_godina_roka'].unique():
        godina_df = df[df['skolska_godina_roka'] == godina]
        izaslo = []
        prijavilo = []
        for mesec in meseci_:
            mesec_df = godina_df[df['tip_roka'] == mesec]
            prijavilo.append(sum(mesec_df['ukupno_prijavilo']))
            izaslo.append(sum(mesec_df['ukupno_izaslo']))
        po_godinama[godina]={
            'godina' : godina,
            'izaslo' : izaslo,
            'prijavilo' : prijavilo
        }
    return po_godinama
        



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

def custom_multitrend_plot(data_list , title="",  ylabel="", xlabel="", name=""):
    figure(figsize=(8, 6), dpi=300)
    labels = ['јануар', 'фебруар', 'јун', 'јул','август', 'септембар', 'октобар']
    ticks = range(len(labels))
    plt.figure(tight_layout=True)
    plt.xticks(ticks, labels)
    for data in data_list:
        print(data['opis'])
        plt.plot(data['data'], 'o-', linewidth=2, color=data['color'], label = data['opis'])
    plt.xlabel(xlabel)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid()
    plt.savefig('Grafici/'+name+'_grafik.png')