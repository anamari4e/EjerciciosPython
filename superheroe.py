puede_volar= input("Tu super heroe puede volar")
es_humano= input("Tu super heroe es humano")
usa_mascara=input("Tu super heroe usa mascara")

if puede_volar =="si": 
    if es_humano =="si":      
        if usa_mascara=="si":
            print("IROMAN") 
        else:
            print("CAPITAN MARVEL")       
    else:
        if usa_mascara =="si":
            print("RONAN ACUSADOR")
        else:
            print("VISION")
else: 
    if es_humano =="si":
        if usa_mascara =="si":
            print("SPIDERMAN")
        else:
            print("HULK")
    else:
        if usa_mascara =="si":
            print("BLACK BOLT")
        else:
            print("THANOS")