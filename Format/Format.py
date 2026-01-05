# Formatação de strings usando o método format() com parâmetros nomeados
a = "A"
b = "B"
c = 7.4652

# Implementando parametros nomeados na formatação
formato = 'a={nome1}, b={nome2}, c={nome3:.2f}'.format(nome1=a, nome2=b, nome3=c)

print(formato)