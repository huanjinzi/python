import webbrowser
import time

total_breaks = 3
break_count = 0

while(break_count < total_breaks):
    time.sleep(5)
    webbrowser.open("https://music.163.com/#/song?id=317868")
    break_count = break_count + 1
