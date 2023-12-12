
#First step: build basic structure
messages= ('[{100001,[{0,-1,"",100}],[{"eve",100}]},'
           '{100002,[{100001,0,"eve",25}],[{"bob",25},{"eve",75}]},'
           '{100003,[{100002,0,"bob",25}],[{"eve",5},{"alice",20}]},'
           '{100004,[{0,-1,"",50}],[{"alice",50}]},'
           '{100005,[{0,-1,"",50}],[{"alice",50}]},'
           '{100006,[{0,-1,"",50}],[{"alice",50}]},'
           '{100007,[{100005,0,"alice",5}],[{"bob",5},{"alice",45}]},'
           '{100012,[{0,-1,"",50}],[{"alice",50}]},'
           '{100008,[{100006,0,"alice",15}],[{"eve",5},{"bob",10},{"alice",35}]},'
           '{100009,[{0,-1,"",50}],[{"bob",50}]},{100011,[{100003,1,"alice",10}],[{"bob",10},{"alice",10}]}]')
messages = messages.replace('{','[')
messages = messages.replace('}',']')
messages = eval(messages)
name = 'alice'
trades = messages

# first index: trade
# second index: 0=id 1=trade_in_list 2=trade_out_list
# third index: trade_in or trade_out
# fourth index: trade_in= {0=id, 1=out_index, 2=donator, 3=amount}
# fourth index: trade_out= {0=acceptor, 1=amount, 2=used}

#Second step: put 'used' attribute into trade_out
for i in range(len(trades)): #to trade
    for j in range(len(trades[i][2])): #to trade_out
        trades[i][2][j].append(False) #add 'used' attribute

#Third step: ergodic all trade_in and set corresponding 'used' as True
for i in range(len(trades)): #to trade
    for j in range(len(trades[i][1])): #to trade_in
        trade_in = trades[i][1][j]
        if trade_in[2] == name and trade_in[0] != 0: #search corresponding name
            target_id = trade_in[0]
            target_index = trade_in[1]
            for k in range(len(trades)):
                if trades[k][0] == target_id:
                    trades[k][2][target_index][2] = True

#Fourth step: calculate the amount
money = 0
for i in range(len(trades)): #to trade
    for j in range(len(trades[i][2])): #to trade_out
        trade_out = trades[i][2][j]
        if trade_out[0] == name and trade_out[2] == False: #only unused is money
            money += trade_out[1]
print(money)
