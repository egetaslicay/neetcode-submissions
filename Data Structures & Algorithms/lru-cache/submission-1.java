public class Node { 

int key; 
int val; 
Node prev;
Node next;

    public Node(int key, int val){ 
        this.key = key;
        this.val = val; 
        this.prev = null;
        this.next = null;

    }
}

class LRUCache {
    int capacity;
    HashMap<Integer, Node> cache;
    Node left;
    Node right;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>(); 
        this.left = new Node(0,0);
        this.right = new Node(0,0); 
        this.left.next = this.right; 
        this.right.prev = this.left;
    }
    
    public int get(int key) {
        if(cache.containsKey(key)){ 
            Node node = cache.get(key);
            remove(node);
            insert(node); 
            return node.val;     
        } else { 
            return -1;
        }
        
    }

    // remove from the list
    public void remove(Node node){ 
        Node next = node.next; 
        Node prev = node.prev;
        next.prev = prev;
        prev.next = next;
    }

    // insert to the right
    public void insert(Node node){ 
       Node oldMRU = this.right.prev; 
       oldMRU.next = node; 
       node.prev = oldMRU; 
       node.next = this.right;
       this.right.prev = node; 
    }
    
    public void put(int key, int value) {
        if(cache.containsKey(key)){ 
            remove(cache.get(key)); 
        }
        Node newNode = new Node(key, value); 
        cache.put(key, newNode); 
        insert(newNode); 

        if(cache.size() > capacity){ 
            Node lru = this.left.next;
            remove(lru);
            cache.remove(lru.key); 
        }
        
    }
}
