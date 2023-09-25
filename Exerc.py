
import math

tamanho_area = float(input("Digite a área da parede em metros quadrados: "))

cobertura_por_litro = 12
tamanho_lata = 18

litros_necessarios = tamanho_area * cobertura_por_litro
latas_necessarias = math.ceil(litros_necessarios / tamanho_lata)
preco_total = latas_necessarias * 80

print(f"Para uma parede de área {tamanho_area:.2f} metros quadrados, você vai precisar de {latas_necessarias} latas, com o custo de R$ {preco_total:.2f}.")
