# TODO Найдите количество книг, которое можно разместить на дискете
byte = 4*25*50*100
megabyte = byte/1024**2
number = 1
while megabyte <= 1.44:
    megabyte+=megabyte
    number+=1
print("Количество книг, помещающихся на дискету:", number)
