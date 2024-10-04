sorteio = {1, 23}

sorteio.add(25)  # {1, 23, 25}
print(sorteio)

sorteio.add(42)  # {1, 23, 25, 42}
print(sorteio)

# Como 25 já existia, ele é ignorado e o set permanece com os mesmos valores
sorteio.add(25)  # {1, 23, 25, 42}
print(sorteio)
