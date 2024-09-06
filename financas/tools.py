import pandas as pd
# import multiprocessing
import concurrent.futures

def copy_table(tabela: list[dict] | pd.DataFrame):
    if isinstance(tabela, list):
        pd.DataFrame(tabela).to_clipboard(excel=True, sep=';', index=False, decimal=',')

    if isinstance(tabela, pd.DataFrame):
        tabela.to_clipboard(excel=True, sep=';', index=False, decimal=',')


def paralelo(func, parameters):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(func, *parameter) for parameter in parameters]

        results = []
        for i, future in enumerate(concurrent.futures.as_completed(futures)):
            results.append(future.result())
            print(i, end='\r')

    return results