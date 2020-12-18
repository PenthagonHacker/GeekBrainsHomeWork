seconds = int(input('Введите кол-во секунд: '))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
remainedsec = (seconds % 3600) % 60

print('{:02d}:{:02d}:{:02d}'.format(hours, minutes, remainedsec))



# Альтернативный способ
# import time
#
# seconds = int(input('Введите кол-во секунд: '))
# newtime = time.strftime('%H:%M:%S', time.gmtime(seconds))
# print(f'Данное кол-во секунд соответствует: {newtime}')
# print(time.gmtime(seconds))
