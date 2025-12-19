'''
ENCONTRAR LA SEGUNDA NOTA MAS BAJA EN LA LISTA DE ESTUDIANTES,
PASANDO NAME, SCORE
'''

student_list = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    student_list.append([name, score])
        
scores = set([score for name, score in student_list])
ordered_scores = sorted(scores)
second = ordered_scores[1]
    
filter_name = [name for name, score in student_list if score == second]
filter_name.sort()
        
for name in filter_name:
    print(name)