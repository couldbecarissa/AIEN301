class Game:
     def __init__ (self):
        self . initialize_game()
     def initialize_game(self):
        self.current_state = [['.','.','.'] ,
                                ['.','.','.'] ,
                                ['.','.','.']]

        self.player_turn = 'X'

     def draw_board(self):
      print("\n")
      for i in range(0, 3):
        print(f" {self.current_state[i][0]} | {self.current_state[i][1]} | {self.current_state[i][2]} ")
        if i < 2:
            print("-----------")
      print("\n")

     def validity(self,px,po):
        if px<0 or po<0 or px>2 or po>2:
            return False
        elif self.current_state[px][po]!='.':
            return False
        else: return True

     def is_over(self):
        #Vertical WIN
        for i in range(0,3):
            if(self.current_state[0][i]!='.' and self.current_state[0][i]==self.current_state[1][i]==self.current_state[2][i]):
                return self.current_state[0][i]
        #Horizontal WIN
        for i in range(0,3):
            if self.current_state[i]==['X','X','X']:return 'X'
            elif self.current_state[i]==['O','O','O']:return 'O'
        #Diagonal WIN
        if self.current_state[0][0] != '.' and self.current_state[0][0] == self.current_state[1][1] == self.current_state[2][2]:
            return self.current_state[0][0]
        if self.current_state[0][2] != '.' and self.current_state[0][2] == self.current_state[1][1] == self.current_state[2][0]:
            return self.current_state[0][2]
        
    # Check if board is full
        return '.' if all(self.current_state[i][j] != '.' for i in range(3) for j in range(3)) else None

     def min_alpha_beta(self,alpha,beta):
        minv=2
        qx=None
        qo=None
        result=self.is_over()
        if result=='X':
            return (-1,0,0)
        elif result=='O': return (1,0,0)
        elif result=='.': return (0,0,0)

        for i in range(0,3):
            for j in range(0,3):
                if self.current_state[i][j]=='.':
                    self.current_state[i][j]='X'
                    (m,max_i,max_j)=self.max_alpha_beta(alpha,beta)
                    if m<minv:
                        minv=m
                        qx=i
                        qo=j
                    self.current_state[i][j]='.'
                    if minv<=alpha:
                        return (minv,qx,qo)
                    if minv<beta:
                        beta=minv
        return (minv,qx,qo)
     
     def max_alpha_beta(self,alpha,beta):
        maxv=-2
        qx=None
        qo=None
        result=self.is_over()
        if result=='X':
            return (-1,0,0)
        elif result=='O': return (1,0,0)
        elif result=='.': return (0,0,0)

        for i in range(0,3):
            for j in range(0,3):
                if self.current_state[i][j]=='.':
                    self.current_state[i][j]='O'
                    (m,min_i,min_j)=self.min_alpha_beta(alpha,beta)
                    if m>maxv:
                        maxv=m
                        qx=i
                        qo=j
                    self.current_state[i][j]='.'
                    if maxv>=beta:
                        return (maxv,qx,qo)
                    if maxv>alpha:
                        alpha=maxv
        return (maxv,qx,qo)
     
     def play(self):
         while True:
             self.draw_board()
             self.result=self.is_over()
             if self.result!=None:
                 if self.result=='X': print("X wins!!!!")
                 elif self.result=='O':print("O wins!!!!!")
                 elif self.result=='.':print("TIEEEEEEE!!!!!!!!!!!")
                 self.initialize_game()
                 return 
             if self.player_turn=='X':
                 while True:
                     (m,qx,qo)=self.min_alpha_beta(-2,2)
                     qx=int(input("X coordinate please:"))
                     qo=int(input("Y coordinate:"))
                     if self.validity(qx,qo):
                         self.current_state[qx][qo]='X'
                         self.player_turn='O'
                         break
                     else: print("Invalid move!")
             else:
                 (m,qx,qo)=self.max_alpha_beta(-2,2)
                 self.current_state[qx][qo]='O'
                 self.player_turn='X'


MAX, MIN = 1000, -1000

def alpha_beta_pruning(depth, node_index, maximizing_player, values, alpha, beta):
    # Base case - leaf node or maximum depth reached
    if depth == 3:
        return values[node_index]
    
    if maximizing_player:
        best = MIN
        for i in range(0, 2):
            val = alpha_beta_pruning(depth + 1, node_index * 2 + i, 
                                   False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            
            # Alpha Beta Pruning
            if beta <= alpha:
                break
        return best
    
    else:
        best = MAX
        for i in range(0, 2):
            val = alpha_beta_pruning(depth + 1, node_index * 2 + i,
                                   True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            
            # Alpha Beta Pruning
            if beta <= alpha:
                break
        return best

# Example usage
if __name__ == "__main__":
    g=Game()
    g.play()