def second_to_print(val):
    if val<10:
        return '0'+str(val)
    else:
        return str(val)


class Timer:
    def __init__(self,hora=0,minuto=0,segundo=0):
        #
        # Escribir código aquí
        #
        self.__hora=hora
        self.__minuto=minuto
        self.__segundo=segundo

    def __str__(self):
        #
        # Escribir código aquí
        #
        return f'{second_to_print(self.__hora)}:{second_to_print(self.__minuto)}:{second_to_print(self.__segundo)}'

    def next_second(self):
        #
        # Escribir código aquí
        #
        self.__segundo+=1
        if self.__segundo>59:
            self.__segundo=0
            self.__minuto+=1
            if self.__minuto>59:
                self.__minuto=0
                self.__hora+=1
                if self.__hora>23:
                    self.__hora=0
        

    def prev_second(self):
        #
        # Escribir código aquí
        #
        self.__segundo-=1
        if self.__segundo<0:
            self.__segundo=59
            self.__minuto-=1
            if self.__minuto<0:
                self.__minuto=59
                self.__hora-=1
                if self.__hora<0:
                    self.__hora=23
        


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
    