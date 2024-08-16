class WeekDayError(Exception):
    pass
	

class Weeker:
    #
    # Escribir código aquí.
    #
    __week=['Lun','Mar','Mie','Jue','Vie','Sab','Dom']

    def __init__(self, day):
        #
        # Escribir código aquí.
        #
        if day not in self.__week:
            raise WeekDayError
        else:
            self.__day=day

    def __str__(self):
        #
        # Escribir código aquí.
        #
            return f'{self.__day}'

    def add_days(self, n):
        #
        # Escribir código aquí.
        #
        pos=self.__week.index(self.__day)
        pos_new=pos+n
        if pos_new > 6:
            x=(pos_new)%7
            pos_new=x
        self.__day=self.__week[pos_new]

    def subtract_days(self, n):
        #
        # Escribir código aquí.
        #
        pos=self.__week.index(self.__day)
        pos_new=pos-n
        if pos_new < 0:
            x=(pos_new)%7
            pos_new=x
        self.__day=self.__week[pos_new]


try:
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Lunes')
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")
    