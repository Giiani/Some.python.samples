def chessValidator(chesttable):
    WPieces, BPieces = 0,0
    BKing, WKing = 0,0
    WPawn,BPawn=0,0
    spaces, check = [],True
    
    for x in ('a','b','c','d','e','f','g','h'):
        for y in range(1,9):
            spaces.append(x+str(y))
            
    for space,piece in chesttable.items():
        
        if space not in spaces:
            print('Space is wrong: ' + space + ' ' + piece)
            check=False
        if piece=='bking':
            BKing+=1
        if piece=='wking':
            WKing+=1
        if piece=='bpawn':
            BPawn+=1
        if piece=='wpawn':
            WPawn+=1
        if piece.startswith('w'):
            WPieces+=1
        if piece.startswith('b'):
            BPieces+=1
        
    if BKing != 1:
        print('More than one black king in the board')
        check=False
    if WKing != 1:
        print('More than one white king in the board')
        check=False
    if BPawn > 8:
        print('More black pawns than is expected in the board')
        check=False
    if WPawn > 8:
        print('More white pawns than is expected in the board')
        check=False
    if WPieces > 16:
        print("The board is invalid have more than 16 white pieces")
        check=False
    if BPieces > 16:
        print("The board is invalid have more than 16 black pieces")
        check=False 
        
    if check:
        return True
    else:
        return False

board = {'e3': 'wking', 'c6': 'wqueen',
     'g2': 'bbishop', 'd2': 'bqueen', 'g3': 'bking',
     'a1': 'bpawn', 'm1': 'bpawn', 'c1': 'bpawn', 'd1': 'bpawn', 
     'e1': 'bpawn', 'f1': 'bpawn', 'g1': 'bpawn', 'h1': 'bpawn', 
     'e2': 'bpawn', 'a2': 'bpawn'}

print(chessValidator(board))
        
    
    
    
    