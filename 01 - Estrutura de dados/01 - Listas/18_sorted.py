linguagens = ["python", "js", "c", "java", "csharp"]

# função built-in do python que é equivalente ao sort
print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]
