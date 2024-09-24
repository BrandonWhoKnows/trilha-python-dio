linguagens = ["python", "js", "c", "java", "csharp"]
# por padrão, ordena strings em ordem alfabética
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
# ordena a lista em ordem alfabética e inverte essa ordem, exibindo o contrário da ordem alfabética
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
# ordena a lista em ordem crescente de acordo com o tamanho do elemento
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
# reverte a ordem do sort anterior, ou seja, ordena em ordem decrescente de acordo com o tamanho do elemento
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)
