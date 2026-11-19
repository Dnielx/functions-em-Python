def conta(nota1, nota2):
    return (nota1 + nota2) / 2

#conta la em baixo media = conta(nota1, nota2) tem relaçao com esse funçao aqui de cima, que é a conta da media, que é a soma das notas dividido por 2
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
    resultado = notas(meda)

    print(resultado)
    print("Obrigado por usar a calculadora de média escolar!")


main()
