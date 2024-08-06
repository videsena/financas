import pandas as pd

def copy_table(tabela: list[dict] | pd.DataFrame):
    if isinstance(tabela, list):
        pd.DataFrame(tabela).to_clipboard(excel=True, sep=';', index=False, decimal=',')

    if isinstance(tabela, pd.DataFrame):
        tabela.to_clipboard(excel=True, sep=';', index=False, decimal=',')
