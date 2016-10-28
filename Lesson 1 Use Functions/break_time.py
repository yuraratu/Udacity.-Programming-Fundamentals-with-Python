import time
import webbrowser

print('Program started at ' + time.ctime())

breaks = 3
break_duration = 10

for b in range(0, breaks):
    time.sleep(break_duration)
    webbrowser.open('https://www.google.co.uk/')
    print(str(b) + ' time link is opened at ' + time.ctime())
