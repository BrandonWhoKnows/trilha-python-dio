# quando não uso a classe tuple, é uma boa prática adicionar uma vírgula mesmo depois do último item para que o interpretador não se perca
frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)
print(pais)
