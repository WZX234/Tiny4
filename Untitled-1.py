fo = open("C:\\Users\\dell\\Desktop\\hex.txt", "w")
while True:
    a = input("\033[36mnumber: \033[0m")
    if a == "q":
        break
    a = str(hex(int(a,2))[2:] + " ")
    print("\033[33m" + a + "\033[0m")
    fo.write(a)
fo.close()
