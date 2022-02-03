import os, time

def print_paint(times, string):
    for i in range(times):
        time.sleep(0.01)
        result1 = string * i
        #result1 = "                                                            *" * i
        #result1 = "|||||||||||||||||||||------------------------@@@@@@@@@@@@@@@@@@@@@----------------------|||||||||||||||||||||" * i
        print(result1)
    os.system("pause")

"""
result2 = "hei"
print(result2[1])
"""




