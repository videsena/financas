import pandas as pd
import multiprocessing

def copy_table(tabela):
    if isinstance(tabela, list):
        pd.DataFrame(tabela).to_clipboard(excel=True, sep=';', index=False, decimal=',')

    if isinstance(tabela, pd.DataFrame):
        tabela.to_clipboard(excel=True, sep=';', index=False, decimal=',')

def paralelo(func, parameters):
    with multiprocessing.Pool() as pool:
        results = pool.map(func, parameters)

    return results