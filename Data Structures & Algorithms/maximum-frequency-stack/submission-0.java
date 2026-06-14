class FreqStack {
    List<Integer> stack; 
    Map<Integer, Integer> freqMap;

    public FreqStack() {
    stack = new ArrayList<>();
    freqMap = new HashMap<>(); 
    }
    
    public void push(int val) {
    stack.add(val);
    freqMap.put(val, freqMap.getOrDefault(val, 0)+1); 
        
    }
    
    public int pop() {
    int max = 0; 
    for(Map.Entry entry : freqMap.entrySet()){ 
    max = Math.max((int) entry.getValue(), max); 
    }

    for(int i = stack.size()-1; i >= 0; i--){ 
        if(freqMap.get(stack.get(i)) == max){ 
        int result = stack.get(i); 
        stack.remove(i);
        freqMap.put(result, freqMap.get(result)-1);
        return result;
        }
    }
    return -1;
    }
 
   
    }
/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack obj = new FreqStack();
 * obj.push(val);
 * int param_2 = obj.pop();
 */