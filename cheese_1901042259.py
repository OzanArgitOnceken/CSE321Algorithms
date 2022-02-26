class cheese:
    def __init__(self,weight,price):
        self.weight=weight
        self.price=price
        self.cost=price/weight
    def __lt__(self,other):
        return self.cost<other.cost

def greedy(wei,pri,cap):
    val=[]
    for i in range(len(wei)):
        val.append(cheese(wei[i],pri[i]))
    val.sort(reverse=True)
    tempPri=0
    tempCap=0
    for i in range(len(val)):
        if tempCap+val[i].weight<=cap:
            tempPri+=val[i].price
            tempCap+=val[i].weight
        else:
            left=cap-tempCap
            tempPri+=left*val[i].cost
            break
    return tempPri
weight=[10,40,15,50]
price=[60,40,100,120]
capacity=50
maxValue =greedy(weight, price, capacity)
print("Maximum value is =", maxValue)