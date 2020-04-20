import random

totalnum = 25
faltantes = 0
escolhidos= []
matriz = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
sorteio =[]
novalista = []
nova_matriz=[]

choisen = 0
while choisen != 5:
    print('''   
    >>>>>>>> $ PROGRAMA  Sortear LOTOFÁCIL $ <<<<<<<<<<<<<
            
            [5] SORTEIO DE 15 NUMEROS
            [6] SORTEIO DE 16 NUMEROS
    
    >>>>>>>>>>>>>>>>> $MARCOS SOUZA 2019$ <<<<<<<<<<<<<<<< \n\n''')


    choisen = int(input(" Digite a opção desejada \n\n"))
    if choisen == 5:
        faltantes = 15 - 5 
        for faltantes in (range(choisen)):
            escolhidos = int(input("Digite os 5 Numeros desejar ganhar $ \n"))
            novalista.append(escolhidos)
            print("Você escolheu {} para seu sorteio".format(novalista))
            unicos = list(set(matriz) - set(novalista))
        #Efetua Sorteio na lista sem numeros repetidos
        sorteio=random.sample(unicos,k=10)
        resultado = sorteio + novalista
        #Ordena os numeros para o resultado final
        resultado_ordenado = sorted(resultado)
        print(''' 

        *+*+*+*+*+*+*+*+*+*+*+  SORTEIO DA LOTOFÁCIL +*+*+*+*+*+*+*+*+*+*+*+*+*+ 
                                                                            
        *+          ->>>>>>> Seus números da sorte são $:   <<<<<<-           +*   
             {}                                                                           
        +*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
        
        '''.format(resultado_ordenado))
        #print(escolhidos)

        choisen = int(input(" Digite a opção desejada \n\n"))
    elif choisen == 6:
        faltantes = 16 - 5 
        for faltantes in (range(choisen)):
            escolhidos = int(input("Digite o nº desejar ganhar $ \n"))
            novalista.append(escolhidos)
            print("Você escolheu {} para seu sorteio".format(novalista))
            unicos = list(set(matriz) - set(novalista))
        #Efetua Sorteio na lista sem numeros repetidos
        sorteio=random.sample(unicos,k=11)
        resultado = sorteio + novalista
        #Ordena os numeros para o resultado final
        resultado_ordenado = sorted(resultado)
        print(''' 

        *+*+*+*+*+*+*+*+*+*+*+  SORTEIO DA LOTOFÁCIL +*+*+*+*+*+*+*+*+*+*+*+*+*+ 
                                                                            
        *+          ->>>>>>> Seus números da sorte são $:   <<<<<<-           +*   
             {}                                                                           
        +*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
        
        '''.format(resultado_ordenado))
        #print(escolhidos)
    else:
        print("numero errado")