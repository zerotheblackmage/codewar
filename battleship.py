# https://www.codewars.com/kata/58d06bfbc43d20767e000074/train/python
def damaged_or_sunk (board, attacks):
    print(board)
    print(attacks)
    board.reverse()
    hits = []
    targets = {}
    hp = {}
    results = { 'sunk': 0, 'damaged' : 0, 'not_touched' : 0, 'points': float(0)}
    for a in attacks:
        x = (a[0] -1)
        y = (a[1] -1)
        tar = board[y]
        if tar[x] != 0:
            hits.append(tar[x])
 
    for i in hits:
        if i not in targets:
            targets[i] = hits.count(i)
            
    for i in board:
        for j in i:
            if not j == 0:
                if j not in hp:
                    hp[j] = 1
                else:     
                    hp[j] += 1

    for key in hp:
        try:
            if hp[key] > targets[key]: 
                print("hit, no kill")
                results['points'] += 0.5
                results['damaged'] += 1
            elif hp[key] == targets[key]:
                print("sunk")
                results['points'] += 1
                results['sunk'] += 1                
        except:
            print("missed")
            results['points'] -= 1
            results['not_touched'] += 1  
            continue
        
    return results
