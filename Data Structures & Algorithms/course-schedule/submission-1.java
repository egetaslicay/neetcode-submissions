class Solution {

    public Map<Integer, List<Integer>> preMap = new HashMap<>(); 
    public Set<Integer> visited = new HashSet<>();


    public boolean canFinish(int numCourses, int[][] prerequisites) {
        
        for(int i = 0; i < numCourses; i++){ 
        preMap.put(i, new ArrayList<>());   
        }

        for(int[] pre : prerequisites){ 
        preMap.get(pre[0]).add(pre[1]); 
        }

        for(int c = 0; c < numCourses; c++){ 
            if(!dfs(c)){ 
                return false;
            }
        }

        return true;
    }

    public boolean dfs(int course){ 
        if(visited.contains(course)){ 
            return false;
        }

        if(preMap.get(course).isEmpty()){
            return true;        
        }

        visited.add(course); 

        List<Integer> preReqs = new ArrayList<>(preMap.get(course)); 
        for(int i = 0; i < preReqs.size(); i++){ 
            if(!dfs(preReqs.get(i))){
                return false;
            }
        }

        visited.remove(course);
        preMap.put(course, new ArrayList<>());
        return true;
       
    }


}
