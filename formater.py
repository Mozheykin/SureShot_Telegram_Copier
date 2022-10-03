from sql import Transaction

def format_message(id:int, message: str) -> Transaction | None:
    try:
        TP1, TP2, TP3, TP4 = 0, 0, 0, 0
        Order, Where, Emmet, CMP, SL, Risk, Change_line = '', '', '', 0, 0, 0, []
        if message.startswith('['):
            _, message = message.split('\n', 1)
        if 'BUY' in message or 'SELL' in message:
        #if message.startswith('BUY') or message.startswith('SELL'):
            lines = message.split('\n')
            for line in lines:
                if 'BUY' in line or 'SELL' in line:
                #if line.startswith(('BUY', 'SELL')):
                    count = len(line.split())
                    if 'LIMIT' in line:
                        Emmet, Order, Where, CMP = line.split(' ')
                    elif count == 2:
                        Emmet, Order = line.split(' ')
                    elif count == 3:
                        Emmet, Order, CMP = line.split()
                    #Order, Where, Emmet, CMP = line.split(' ', 3)
                    #CMP = CMP.split()[2][:-1]
                elif line.startswith('TP:'):
                    TP1 = line.split()[1]
                elif line.startswith('TP1:'):
                    TP1 = line.split()[1]
                elif line.startswith('TP2:'):
                    TP2 = line.split()[1]
                elif line.startswith('TP3:'):
                    TP3 = line.split()[1]
                elif line.startswith('TP4:'):
                    TP4 = line.split()[1]
                elif line.startswith('SL:'):
                    SL = line.split()[1]
                elif line.startswith('Risk:'):
                    Risk = line.split()[1][:-1]
            return Transaction(id_=id, Order=Order, Where=Where, Emmet=Emmet, CMP=float(CMP), TP1=float(TP1), TP2=float(TP2), TP3=float(TP3), TP4=float(TP4), SL=float(SL), Risk=float(Risk), Update='')
        elif message.startswith('Update'):
            lines = message.split('\n')
            for line in lines:
                if line.startswith('Update'):
                    Order, Emmet, CMP = lines[0].split(' ', 2)
                    CMP = CMP.split()[2][:-1]
                elif line.startswith('TP:'):
                    TP1 = line.split()[1]
                elif line.startswith('TP1:'):
                    TP1 = line.split()[1]
                elif line.startswith('TP2:'):
                    TP2 = line.split()[1]
                elif line.startswith('TP3:'):
                    TP3 = line.split()[1]
                elif line.startswith('TP4:'):
                    TP4 = line.split()[1]
                elif line.startswith('SL:'):
                    SL = line.split()[1]
                elif line.startswith('ADJUST'):
                    Change_line = line.split()
            return Transaction(id_=id, Order=Order, Where=f'{Change_line[1]}', Emmet=Emmet, CMP=float(CMP), TP1=float(TP1), TP2=float(TP2), TP3=float(TP3), TP4=float(TP4), SL=float(SL), Risk=float(0), Update=Change_line[-1])
        elif 'close' in message.lower():
            if 'full' in message.lower():
                return Transaction(id_=id, Order='Close', Where='NOW', Emmet='all', CMP=float(CMP), TP1=float(0), TP2=float(0), TP3=float(0), TP4=float(0), SL=float(0), Risk=float(0), Update='')
            else:
                Emmet, Order, Other = message.split(' ', 2)
                #CMP = Other.split()[2][:-1]
                return Transaction(id_=id, Order='Close', Where='NOW', Emmet=Emmet, CMP=float(CMP), TP1=float(0), TP2=float(0), TP3=float(0), TP4=float(0), SL=float(0), Risk=float(0), Update='')
    except Exception:
        return None


if __name__ == '__main__':
    #print(format_message(id=2, message='BUY NOW NAS100 (CMP : 12140)\nTP: 12500\nSL: 11800\nRisk: 2%'))
    #print(format_message(id=2, message='BUY NOW NAS100 (CMP : 12140)\nTP1: 12501\nTP2: 12502\nTP3: 12503\nTP4: 12504\nSL: 11800\nRisk: 2%'))
    #print(format_message(id=2, message='SELL NOW NAS100 (CMP : 12140)\nTP: 12500\nSL: 11800\nRisk: 2%'))
    #print(format_message(id=5, message='Update SPX500 (CMP : 12140)\nTP: 12500\nSL: 11800\nADJUST SL TO 3848'))
    #print(format_message(id=6, message='Close NOW NAS100 (CMP : 12140)\nResult pips: -300'))
    #print(format_message(id=6, message='Close NOW NAS100 (CMP : 12140)'))
    print(format_message(id=1, message='[Forwarded from Sureshot FX VIP]\nUSDCAD SELL LIMIT 1.37678\n\nSL:  1.38390\nTP:  1.36382\n--Trade by Matthew'))
    print(format_message(id=2, message='[Forwarded from Sureshot FX VIP]\nXAUUSD BUY LIMIT 1633\n\nSL:  1621\nTP:  1655\n--Trade by Grace'))
    print(format_message(id=3, message='[Forwarded from Sureshot FX VIP]\nGBPUSD BUY\n\nSL:  1.0645\nTP:  1.1260\n--Trade by Lucas'))
    print(format_message(id=4, message='USDCAD SELL LIMIT 1.37678\n\nSL:  1.38390\nTP:  1.36382\n--Trade by Matthew'))
    print(format_message(id=5, message='XAUUSD BUY LIMIT 1633\n\nSL:  1621\nTP:  1655\n--Trade by Grace'))
    print(format_message(id=6, message='GBPUSD BUY\n\nSL:  1.0645\nTP:  1.1260\n--Trade by Lucas'))
    print(format_message(id=7, message='USDCAD SELL 1.3639\n\nSL:  1.3712\nTP:  1.3497\n--Trade by Grace'))
    print(format_message(id=8, message='Full close'))
    print(format_message(id=9, message='EURUSD CLOSE HALF 30 PIPS'))
