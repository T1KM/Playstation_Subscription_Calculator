
#Menu
def menu():
    global typy,pick
    cost = [0,7.99,20.99,64.99,11.99,33.99,107.99,13.99,39.99,124.99]
    length=[0,1,3,12,1,3,12,1,3,12]
    typy=["None","Normal","Normal","Normal","Plus","Plus","Plus","Extra","Extra","Extra"]
    print("Welcome to PlayStation Plus Calculator")
    print("   Which subscription do you want to use?")
    print('''
 Normal 1-(1month) 2-(3month) 3-(12month)
 Plus   4-(1month) 5-(3month) 6-(12month)
 Extra  7-(1month) 8-(3month) 9-(12month)''')
    try:
        pick = int(input(">"))
        left = int(input(" how many days are left?:"))
    except:
        menu()
    if left > (cost[pick]* 30):
        print("you've acrossed the line.")
        try:
            left = int(input(" how many days are left?(you cannot add more days than the Subscription.):"))
            if left > (cost[pick]* 30):
                raise ValueError
        except ValueError:
            print("really? same mistake twice?")
            raise ValueError
    if pick < 10 and pick > 0:
        print(pscal(cost[pick], length[pick],left))
#calculator        
def information_maker(a,b,c,d,e,f,g):
    print(f'''
Subscription:{a}
length:{b} month
cost(USD):{c}
cost(SAR):{d}
Remaining_Days:{e}
RDcost(USD):{f}
RDcost(SAR):{g}
    ''')
    value = float(input("type here the percent value you want to get\n(0.1 =10%),(0.3=30%),(1=100%):>"))
    print(g * value)
    return

def pscal(cost,months,left):
    result = (cost * 3.75) / (months * 30) * left
    print()
    print(f"it worths now:{result}|SAR")
    def information_Q():
        try:
            answer = int(input("do you want information menu?\n 1-yes\n 2-no"))
            if answer == 1:
                information_maker(typy[pick],months,cost,cost *3.75,left,result/3.75,result)
            elif answer ==2:
                print("have a good day sir!")
            else:
                print("value error")
                information_Q()
        except ValueError:
                print("error.")   
    information_Q()       
menu()   
   

    