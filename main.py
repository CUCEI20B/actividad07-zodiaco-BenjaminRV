d=int(input())
m=int(input())
if ((m == 12 and d > 21) or (m == 1 and d < 20)):
    print("capricornio")
elif ((m == 1 and d > 19) or (m == 2 and d < 19)):
    print("acuario") 
elif ((m == 2 and d > 18) or (m == 3 and d < 21)):
    print("piscis") 
elif ((m == 3 and d > 20) or (m == 4 and d < 21)):
    print("aries") 
elif ((m == 4 and d > 20) or (m == 5 and d < 21)):
    print("tauro") 
elif ((m == 5 and d > 20) or (m == 6 and d < 25)):
    print("geminis")
elif ((m == 6 and d > 24) or (m == 7 and d < 23)):
    print("cancer")
elif ((m == 7 and d > 22) or (m == 8 and d < 24)):
    print("leo") 
elif ((m == 8 and d > 23) or (m == 9 and d < 24)):
    print("virgo")
elif ((m == 9 and d > 23) or (m == 10 and d < 23)):
    print("libra")
elif ((m == 10 and d > 22) or (m == 11 and d < 22)):
    print("escorpio") 
elif ((m == 11 and d > 21) or (m == 12 and d < 22)):
    print("sagitario")
