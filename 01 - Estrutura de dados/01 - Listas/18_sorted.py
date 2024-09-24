linguagens = ["python", "js", "c", "java", "csharp"]

# função built-in do python que é equivalente ao sort, com a diferença de que o sorted não altera a lista original
print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]