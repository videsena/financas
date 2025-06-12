import pandas as pd
import os, sys, pathlib

def get_tabela_inss(ano):
    tabela = pd.read_csv(f"{str(pathlib.Path().resolve())}/financas/tabela_inss.csv").to_dict('records')
    tabela = [t for t in tabela if t['ano'] == ano]
    return tabela

def get_tabela_irrf(ano):
    tabela = pd.read_csv(f"{str(pathlib.Path().resolve())}/financas/tabela_irrf.csv").to_dict('records')
    tabela = [t for t in tabela if t['ano'] == ano]
    return tabela