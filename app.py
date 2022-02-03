from tv import *

f1 = str(open("nikita.txt", "r").read())
f2 = open("nikita2.txt", "w")
f2.write(f1[::-1])
f2.close()

#result1 = "|||||||||||||||||||||------------------------@@@@@@@@@@@@@@@@@@@@@----------------------|||||||||||||||||||||"

x = "                                                            *"

print_paint(1, f1)
print_paint(1, str(f2))


