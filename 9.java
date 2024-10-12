class Solution {
    public boolean isPalindrome(int x) {
        if (x<0){
            return false;
        }
        else{
            Deque<Integer> deque = new ArrayDeque<>();
            while(x != 0){
                deque.addLast(x % 10); 
                x = x / 10;
            }
            while (deque.size() > 1){
                int left = deque.removeFirst();
                int right = deque.removeLast();
                if (left != right){return false;}
            }
        }
        return true;
    }
}

class Solution1 {
    public boolean isPalindrome(int x) {
        String str = Integer.toString(x);
        int l = 0;
        int r = str.length() - 1;
        while (l < r){
            if (str.charAt(l) != str.charAt(r)){
                return false;
            }
            l += 1;
            r -= 1;
        }
        return true;
    }
}