from ib_insync import *
from ibapi.order_condition import *

ib = IB()

ib.connect('127.0.0.1', 7496, clientId=15)
contract = []
contract = Stock('AAPL','SMART','USD')

ib.qualifyContracts(contract)

conParams = []

#conParams.append(PriceCondition(0, contract.conId, "SMART", False, 112.0))
lmt = LimitOrder('BUY', 100 ,110, algoStrategy='Adaptive',algoParams=[TagValue('adaptivePriority', 'Normal')],
                 conditions = [PriceCondition(0, contract.conId, exch= "SMART", isMore= True, price = 112)])
# print(lmt)
ib.placeOrder(contract, lmt)

# parent = MarketOrder('BUY', 100,  algoStrategy='Adaptive',algoParams=[TagValue('adaptivePriority', 'Normal')])
# ib.placeOrder(contract, parent)
# def __init__(self, triggerMethod=None, conId=None, exch=None, isMore=None,
#                  price=None):
