# input(ingreasr datos)
# variables: salario bruto,porcentaje-impuesto
salario_bruto=float(input("ingrsar salario bruto:"))
porcentaje_impuesto=float(input("ingresar porcentaje de impuesto:"))
salario_neto=salario_bruto-(salario_bruto*porcentaje_impuesto/100)
print("el salario bruto es",salario_bruto)
print("el porcentaje de impuesto es",porcentaje_impuesto)
print("el salario neto es",salario_neto)