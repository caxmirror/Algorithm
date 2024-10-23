class Solution {
    public boolean isPalindrome(String s) {
        int l = 0;
        int r = s.length()-1;
        while (l < r){
            char leftchar = s.charAt(l);
            char rightchar = s.charAt(r);
            leftchar = Character.toLowerCase(leftchar);
            rightchar = Character.toLowerCase(rightchar);
            
            if(leftchar < '0' || (leftchar > '9' && leftchar < 'a') || leftchar > 'z'){
                l += 1;
                continue;
            }

            if(rightchar < '0' || (rightchar > '9' && rightchar < 'a') || rightchar > 'z'){
                r -= 1;
                continue;
            }

            if(leftchar == rightchar){
                l += 1;
                r -= 1;
                continue;
            }

            else{
                return false;
            }

        }
        return true;
    }
}