notas = input("Digite as notas dos alunos separadas por vírgula: ").split(", ")
notas = [float(nota) for nota in notas]
media = sum(notas) / len(notas)
print(f"Média final da turma: {media:.2f}")

notes = input("Enter the students' grades separated by commas: ").split(", ")
notes = [float(note) for note in notes]
media = sum(notes) / len(notes)
print(f"The class final media is: {media:.2f}")