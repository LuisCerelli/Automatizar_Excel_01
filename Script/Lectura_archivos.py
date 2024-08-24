import pandas as pd

def main():
    df = leer_archivos()
    df = agregar_filtros(df)

    #visualizar_datos(df) 
    exportar_datos(df)

def leer_archivos():
    print('Leyendo archivo')
    import os

    input_cols = [3,4,5,6,7,12]

    path = '../Input'
    filename = input('Ingresar el nombre del archivo: ') + 'csv'
    fullpath = os.path.join(path, filename)

    #Tambien puedes colocar un xlsx y cambiar por pd.read_excel
    df = pd.read_csv('Aca_coloca_la_ruta_de_tu_data_frame.csv',
                 header=0,
                 usecols=input_cols)
    
    return df
    
def agregar_filtros(df):
    print("Agregando filtros")

    df = df[df['Payment'] == 'Cash'] 

    return df

def visualizar_datos(df):
    print("Visualizando los primeros 5 registros")

    df_cols = df.columns

    for col in df_cols:
        print(df[col].head())

def exportar_datos(df):
    print("Exportando archivo procesado")

    df.to_csv('Coloca_la_ruta_donde_este_la_carpeta/Output/ejemplo.csv',
            sep=',',
            header=True,
            index=False)
    
if __name__ == '__main__':
    main()    
    input("\tPROCESO FINALIZADO. Presionar Enter para salir")
