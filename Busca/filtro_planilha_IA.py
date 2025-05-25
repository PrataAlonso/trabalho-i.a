
import pandas as pd

# Carregar a planilha
df = pd.read_excel("C:/Users/joao-/OneDrive/Desktop/Faculdade/Trabalhos/quinto semestre/Lucas/Busca/banco de dados/Registro_Acidentes_Ficticio.xlsx")

df = df.iloc[:20] #limita a navegação do algoritmo pela planilha para os primeiros 20 registros

def aplicar_filtro(df, filtro_tipo, valor): #resultado de filtros
    match filtro_tipo:
        case '1':
            return df[df['Avenida'].str.contains(valor, case=False)]
        case '2':
            return df[df['Marca'].str.contains(valor, case=False)]
        case '3':
            return df[df['Categoria do Veículo'].str.contains(valor, case=False)]
        case '4':
            return df[df['Data'].astype(str).str.contains(valor)]
        case '5':
            return df[df['Horário do Acidente'].str.contains(valor)]
        case _:
            print("Opção inválida.")
            return pd.DataFrame()


def main():
    print("""
Escolha um filtro para aplicar na planilha (primeiros 20 registros):
1 - Avenida
2 - Marca
3 - Categoria do Veículo
4 - Data (formato AAAA-MM-DD)
5 - Horário do Acidente (formato HH:MM)
    """)
    filtro = input("Digite o número da opção desejada: ")
    valor = input("Digite o valor a ser buscado: ")

    resultado = aplicar_filtro(df, filtro, valor)
    
    if not resultado.empty:
        print("\nResultados encontrados:")
        print(resultado)
    else:
        print("Nenhum resultado encontrado.")

if __name__ == "__main__":
    main()
