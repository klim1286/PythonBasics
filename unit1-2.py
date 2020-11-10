seconds = int(input('Введите число: '))
hover = seconds // 3600
minute = (seconds - hover * 3600) // 60
os_seconds = seconds - hover * 3600 - minute * 60
print(f'{hover:02d}:{minute:02d}:{os_seconds:02d}')
