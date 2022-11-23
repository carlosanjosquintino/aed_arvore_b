from B_tree import Search_B_tree

url = "http://repositorio.dados.gov.br/educacao/CADASTRO_MATRICULAS_REGIAO_NORTE_2012.csv"

tree = Search_B_tree(url,1)

tree.get_extension()
tree.get_pandas_df()