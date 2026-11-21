def conta(nota1, nota2):
    return (nota1 + nota2) / 2

#conta la em baixo media = conta(nota1, nota2) tem relaçao com esse funçao 
# aqui de cima, que é a conta da media, que é a soma das notas dividido por 2

#def notas(media): fica com valor (def conta(nota1, nota2)) ele vira a conta a ser executada para achar o resultado. o media que esta destacado valor que atribuimos na função main.
def notas(media):
    if media >= 6.133:
        return f"voce passou com a nota {media:.3f}"
    elif media >= 5.210:
        return f"voce ficou de recuperação com a nota {media:.3f}"
    else:
        return f"voce foi reprovado com a nota {media:.3f}"


def main():
    print("Calculadora de média escolar")

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = conta(nota1, nota2)
    resultado = notas(media)
#media = conta que precisamos exercurta para achar o resultado, precisamos aqui nessa parte do main, dar valor a ela, entao colocamos a função definida no inicio do codigo para buscar resultados 
#resultado = voce coloca a notas(media) aqui pq agora ela nesse passo a passo ja atribuimos que ela vai fazer a conta da media, assim fica mais simples no final colocar esse print(resultado) que vai mostrar o resultado final da media, se passou, ficou de recuperaçao ou foi reprovado.

    print(resultado)
    print("Obrigado por usar a calculadora de média escolar!")


main()
