import heapq
def minimumWait(orders) :
    totalWait = 0
    ordersno = len(orders)
    if ordersno == 0 :
        return 0
    orderpending = []
    currtime = orders[0][0]
    flag = True
    while flag :
        while len(orders) != 0 and orders[0][0] <= currtime :
            order = heapq.heappop(orders)   
            heapq.heappush(orderpending, (order[1], order[0]))
        if len(orderpending) != 0 :
            minwait = heapq.heappop(orderpending)
            waitTime = currtime - minwait[1] + minwait[0]
            totalWait += waitTime
            currtime += minwait[0]
        else :
            currtime += 1
        if len(orderpending) == 0 and len(orders) == 0 :
            flag = False
    return totalWait/ordersno
n=int(input("Enter number of customers:"))
t=[]  #timestamp
l=[]  #durationstamp
orders=[]
for i in range(n):
    T=int(input('Enter arrival time:'))
    L=int(input("Enter manufacturing time:"))
    heapq.heappush(orders,(T,L))
print(int(minimumWait(orders)))