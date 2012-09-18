# Problem 19 - project euler
# How many sundays fell on 1st of month on 20th century (1 Jan 1901 to 31 Dec 2000)

nonLeapYear = [31,28,31,30,31,30,31,31,30,31,30,31] # 365
leapYear = [31,29,31,30,31,30,31,31,30,31,30,31]    # 366
days = {1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',0:'Sunday'}
months = {13:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'Septemper',10:'October',11:'November',12:'December'}
yearDays = 365
leapYearDays = 366

# What is the last day of 1900
var = 1
Sundays = 0
temp = 0
for year in range(1901,2001):
    if not year % 4:
        if year % 100 or not year % 400:
            counter = 2
            for i in leapYear:
                var += i%7
                temp = var%7 +1
                if temp == 7:
                    temp = 0
                if temp == 0:
                    print 'Sunday found on {1}, {0}'.format(year, months[counter])
                    Sundays += 1
                counter += 1
        else:  
            counter = 2          
            for i in nonLeapYear:
                var += i%7
                temp = var%7 +1
                if temp == 7:
                    temp = 0
                if temp == 0:
                    print 'Sunday found on {1}, {0}'.format(year, months[counter])
                    Sundays += 1
                counter += 1
    else:   
        counter = 2         
        for i in nonLeapYear:
            var += i%7
            temp = var%7 +1
            if temp == 7:
                temp = 0
            if temp == 0:
                print 'Sunday found on {1}, {0}'.format(year, months[counter])
                Sundays += 1
            counter += 1
            #temp += i%7 + 1
            #if days[temp] == 'Sunday':
            #    Sundays +=1
    var = var%7
    if var > 6:
        var -= 7
    #print 'Last day in year {0} was {1}'.format(year,days[var])
print '---'
print 'Sundays found: {0}'.format(Sundays)
            
