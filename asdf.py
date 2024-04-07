perviu = int(input('Введите оценку за первый предмет')
vtoroy = int(input('Введите оценку за второй предмет'))
treti = int(input('Введите оценку за третий предмет'))
chetvert = int(input('Введите оценку за четвёртый предмет'))
pyati = int(input('Введите оценку за пятый предмет'))
avg = (perviu + voroy + treti + chetvert + pyati)/5
if avg >= 90:
  print('Отлично')
elif avg >= 80 and avg < 90:
  print('Хорошо')
elif avg >= 70 and avg < 80:
  print'Нормально'
elif avg >=60 and avg < 70:
  prit('Незачёт')
