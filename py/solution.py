from typing import Dict, List, Tuple

from util import Color, Sat, User, Vector3


def solve(users: Dict[User, Vector3], sats: Dict[Sat, Vector3]) -> Dict[User, Tuple[Sat, Color]]:
    """Assign users to satellites respecting all constraints."""
    arr=[[0 for j in range(len(users))] for i in range(len(sats))]
    print(arr)
    solution = {}
    dict1={}  #it stores sattelite to list of users
    beams={} #it stores the number of beams
    for i in sats:
        dict1[i]=[] #empty list
        beams[i]=32 #giving 32 beams
        for j in users:
            if(beams[i]>0): #if there is beam then loop else break
                if(users[j].angle_between(sats[i],sats[i])<=45):# if the angle between user and this sattelite is lesss than 45 than concern it
                    if(beams[i]==32): #simply assign user
                        solution[j]=[]
                        dict1[i].append(j)
                        arr[i][j]=  0# ite will stroe the color only in thsi case red
                        solution[j].append(i)
                        solution[j].append(Color.A)
                    else:
                        if(dict1.get(i) is None): 
                            solution[j]=[]
                            dict1[i].append(j)
                            arr[i][j]= 0
                            solution[j].append(i)
                            solution[j].append(Color.A)
                        else:
                            for k in dict1[i]:
                                thetaList=[] #this contains the list in which between angle 10 there exits other users
                                if(sats[i].angle_between(users[j],k)<=10): #if there exist users assigned different beams color
                                    thetaList.append(k)
                            #now check the length of users if there is one
                            if(len(thetaList)==1):
                                solution[j]=[]
                                dict1[i].append(j)
                                arr[i][j]=1 #blue color
                                solution[j].append(i)
                                solution[j].append(Color.B)
                            elif(len(thetaList)==2):
                                solution[j]=[]
                                dict1[i].append(j)
                                arr[i][j]=2 #green color
                                solution[j].append(i)
                                solution[j].append(Color.C)
                            elif(len(thetaList)==3):
                                 solution[j]=[]
                                 dict1[i].append(j)
                                 arr[i][j]=3 #yellow color
                                 solution[j].append(i)
                                 solution[j].append(Color.D)
                            # else:
                            
                                
                                #user cannot be assigned
                            

            # else:
            #     break
            print(solution)
            print("\n")
    return solution