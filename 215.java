//time: n logk
//space: k
class Solution_best {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(k);
        for(int num: nums){
            minHeap.add(num);
            if (minHeap.size() > k){
                minHeap.poll();
            }
        }
        return minHeap.peek();
    }
}

//time: n logn
//space: n
class Solution_bad {
    public int findKthLargest(int[] nums, int k) {
        // Deque, pull k times
        PriorityQueue<Integer> deque = new PriorityQueue<>((a,b) -> b-a);
        for(int num: nums){
            deque.add(num);
        }
        int res = 0;
        while(k > 0){
            res = deque.remove();
            k -= 1;
        }
        return res;
    }
}