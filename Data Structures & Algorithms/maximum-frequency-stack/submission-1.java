class FreqStack {

    Map<Integer, Integer> freqMap;              // value -> frequency
    Map<Integer, Stack<Integer>> groupMap;      // frequency -> stack of values
    int maxFreq;

    public FreqStack() {
        freqMap = new HashMap<>();
        groupMap = new HashMap<>();
        maxFreq = 0;
    }
    
    public void push(int val) {
        int freq = freqMap.getOrDefault(val, 0) + 1;
        freqMap.put(val, freq);

        if (freq > maxFreq) {
            maxFreq = freq;
        }

        groupMap.computeIfAbsent(freq, k -> new Stack<>()).push(val);
    }
    
    public int pop() {
        int result = groupMap.get(maxFreq).pop();
        freqMap.put(result, freqMap.get(result) - 1);

        if (groupMap.get(maxFreq).isEmpty()) {
            maxFreq--;
        }

        return result;
    }
}
