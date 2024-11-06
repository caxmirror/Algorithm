




// time: n^2 logk
// space: k
class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        //maxheap with cap k
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(k,(a,b) -> b - a );
        for (int i = 0; i < matrix.length; ++i){
            for (int j = 0; j<matrix[0].length;++j){
                maxHeap.add(matrix[i][j]);
                if (maxHeap.size()>k){
                    maxHeap.poll();
                }
            }
        }
        return maxHeap.peek();

        
    }
}