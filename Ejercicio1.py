def menu():
    n1 = [[1,2,0],[3,1,4],[3,0,1]]
    n2 = [[5,6,7,1],[8,9,2,0],[3,6,4,7],[1,6,0,2]]
    n3 = [[2,1,5,0,6],[3,8,2,7,3],[2,0,1,4,5],[3,1,6,9,8],[5,6,3,9,3]]

    print("1")
    print("2")
    print("3")
    escoger = int(input("Escoger un número y saldra la matriz y suma: "))
 
    if (escoger == 1):
            print(n1)
            suma = n1[0][0] + n1[1][1] + n1[2][2] 
            print("La suma de su matriz fue: ",suma)
    elif(escoger == 2):
            print(n2)
            suma = n2[0][0] + n2[1][1] + n2[2][2] + n2[3][3]
            print("La suma de su matriz fue: ",suma)
    elif(escoger == 3):
            print(n3)
            suma = n3[0][0] + n3[1][1] + n3[2][2] + n3[3][3]+ n3[4][4]
            print("La suma de su matriz fue: ",suma)
menu()
    



        
   
