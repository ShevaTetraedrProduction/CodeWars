def make_readable(seconds):
    hours = seconds // 3600
    seconds = hours * 3600
    minutes = seconds // 60
    seconds -= minutes * 60
    x = lambda a: (a, '0' + str(a))[a < 10]  
    return '{}:{}:{}'.format(x(hours), x(minutes), x(seconds))
    #return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)



print (
	make_readable(86399)
)