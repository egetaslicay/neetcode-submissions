class Solution {
    public int maxArea = 0; 

    public int maxAreaOfIsland(int[][] grid) {
    int ROWS = grid.length; 
    int COLS = grid[0].length; 

    for(int r = 0;  r < ROWS; r++){ 
        for(int c = 0; c < COLS; c++) { 
            if(grid[r][c] == 1){ 
            int currArea = dfs(grid, r, c); 
            maxArea = Math.max(currArea, maxArea);
            }

           
        }
      }

      return maxArea;
    }




    public int dfs(int[][] grid, int r, int c){ 
        if(r < 0 || c < 0 || r >= grid.length || c >= grid[0].length){
            return 0;
        }
        if(grid[r][c] == 1){ 
        grid[r][c] = 0; 
        return 1 + dfs(grid, r+1,c) + dfs(grid, r-1, c) + dfs(grid, r, c+1) + dfs(grid, r, c-1);
        } else { 
            return 0;
        }
            
            
         
        

    }
}
