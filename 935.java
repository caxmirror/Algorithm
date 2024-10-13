class Solution {
    public int knightDialer(int n) {
        if(n==1){return 10;}
        Map<Integer,int[]> map = new HashMap<>();
        map.put(1,new int[]{6,8});
        map.put(2,new int[]{7,9});
        map.put(3,new int[]{4,8});
        map.put(4,new int[]{3,9,0});
        map.put(6,new int[]{1,7,0});
        map.put(7,new int[]{2,6});
        map.put(8,new int[]{1,3});
        map.put(9,new int[]{2,4});
        map.put(0,new int[]{4,6});

        Map<Integer,Integer> count = new HashMap<>();
        for(int i = 0;i<=10;i++){
            count.put(i,1);
        }
        count.remove(5);
        
        for(int i = 1;i<n;i++){
            
            Map<Integer,Integer> newcount = new HashMap<>();
            for(int j = 0; j<=10; j++){
            newcount.put(j,0);
            }
            newcount.remove(5);

            for(int key:map.keySet()){ //each num
                int[] keylist = map.get(key);

                for (int updated: keylist) //sub num
                    newcount.put(updated,(newcount.get(updated)+count.get(key))% (7 + 1000000000) ); //update sub num
            }
            
            count = newcount;
            }
    int res = 0;
        for(int key:count.keySet()){
            res += count.get(key);
            res = res % (7 + 1000000000);
        
        }    
    return res;
    }
    
}