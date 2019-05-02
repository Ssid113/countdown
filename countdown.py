from datetime import datetime

def countdown(dateStart: datetime, dateEnd: datetime):
    """
    Эта функция определяет количество дней, часов, минут, секунд между двумя входными датами (datetime)
    Возвращает days, hours, minutes, seconds
    
    This function determines the number of days, hours, minutes, seconds between two input dates (datetime)
    Return days, hours, minutes, seconds
    """
    timedelta = dateEnd - dateStart
    minutes, seconds = divmod(timedelta.seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return timedelta.days, hours, minutes, seconds

def countdownRU(dateStart: datetime, dateEnd: datetime) -> str:
    """
    Эта функция определяет количество дней, часов, минут, секунд между двумя входными датами (datetime).
    Выводит строку с описанием на русском языке.
    nplurals=3; plural=(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2);
    Пример: 0 дней 23 часа 38 минут 44 секунды
    """
    days, hours, minutes, seconds = countdown(dateStart, dateEnd)
    plural = lambda n: (0 if (n%10==1 and n%100!=11) 
                        else ( 1 if (n%10>=2 and n%10<=4 and (n%100<10 or n%100>20)) else 2))
    def funcPlural(n, text):
        return text[plural(n)]
    return ("%d %s %d %s %d %s %d %s" % (days, funcPlural(days, ["день","дня","дней"]), 
                                         hours, funcPlural(hours, ["час","часа","часов"]), 
                                         minutes, funcPlural(minutes, ["минута","минуты","минут"]), 
                                         seconds, funcPlural(seconds, ["секунда","секунды","секунд"])))

def countdownEN(dateStart: datetime, dateEnd: datetime) -> str:
    """
    Эта функция определяет количество дней, часов, минут, секунд между двумя входными датами (datetime).
    Выводит строку с описанием на английском языке.
    nplurals=2; plural=(n != 1);
    Пример: 0 days 1 hour 38 minutes 1 second
    """
    days, hours, minutes, seconds = countdown(dateStart, dateEnd)
    plural = lambda n: (0 if (n==1) else (1))
    def funcPlural(n, text):
        return text[plural(n)]
    return ("%d %s %d %s %d %s %d %s" % (days, funcPlural(days, ["day","days"]), 
                                         hours, funcPlural(hours, ["hour","hours"]), 
                                         minutes, funcPlural(minutes, ["minute","minutes"]), 
                                         seconds, funcPlural(seconds, ["second","seconds"])))

print(countdownRU(datetime.now(), datetime(2019, 5, 3, 16, 0, 0)))
print(countdownEN(datetime.now(), datetime(2019, 5, 3, 16, 0, 0)))
