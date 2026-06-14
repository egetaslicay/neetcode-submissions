class Solution {
    public boolean isValidSudoku(char[][] board) {
    if(board == null){
        return false;
    }

    boolean isValid = true; 


    // check each row by row first. 
    for(int i = 0; i < board.length; i++) { 
        Set<Character> charArray = new HashSet<>(); 
        for(int j = 0; j < board[0].length; j++){ 
            if(charArray.contains(board[i][j])){ 
                return false; 
            } else { 
                if(board[i][j] != '.'){
                charArray.add(board[i][j]); 
                }
            }
        }
    }

    // check each column now
    for(int i = 0; i < board[0].length; i++) { 
        Set<Character> charArray = new HashSet<>(); 
        for(int j = 0; j < board.length; j++){ 
            if(charArray.contains(board[j][i])){ 
                return false; 
            } else {
                if(board[j][i] != '.') {
                charArray.add(board[j][i]);
                } 
            }
        }
    }
    
    // each group has a set now.
    Map<Integer, Set<Character>> groupMap = new HashMap<>(); 
    for(int i = 0; i <= 9; i++){ 
        groupMap.put(i, new HashSet<>());
    }

    for(int i = 0; i < board.length; i++) { 
        for(int j = 0; j < board[0].length; j++){ 
         int group = 0;
         if(i <= 2){ 
            if(j <=2){ group = 1; }
            else if(j <=5){ group = 2; }
            else { group = 3; }
         } else if(i <= 5) { 
             if(j <=2){ group = 4; }
             else if(j <=5){ group = 5; }
             else { group = 6; }

         } else if(i <= 8){ 
            if(j <=2){ group = 7; } 
            else if(j <=5){ group = 8; }
            else { group = 9; }
        }
        
        if(board[i][j] != '.'){ 
           if(groupMap.get(group).contains(board[i][j])){
            return false; 
           } else { 
            groupMap.get(group).add(board[i][j]);
           }
        }    

        }
    }

    return true;








    }
}
