class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        if(!wordList.contains(endWord) || beginWord.equals(endWord)){ 
            return 0;
        }   

        Set<String> words = new HashSet<>(wordList);
        int result = 0;
        Queue<String> q = new ArrayDeque<>();
        q.add(beginWord); 

        while(!q.isEmpty()){ 
            result++; 
            int qSize = q.size();
            for(int i = 0; i < qSize; i++){ 
                String node = q.poll(); 
            if(node.equals(endWord)){ 
                return result;
            }
            for(int j = 0; j < node.length(); j++){ 
                for(char c = 'a'; c <= 'z'; c++){ 
                    if(c == node.charAt(j)){ 
                        continue;
                    }
                    String nei = node.substring(0, j) + c + node.substring(j+1);
                    if(words.contains(nei)){ 
                        q.offer(nei);
                        words.remove(nei);
                    }
                }


            }








            }

        }
        
        return 0;
    }
}
