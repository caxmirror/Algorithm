class Solution {
    public boolean isLongPressedName(String name, String typed) {
        int p1 = 0;
        int p2 = 0;
        while(p1 < name.length() && p2 < typed.length() ){
            if(typed.charAt(p2) != name.charAt(p1)){return false;}
            if(p1+1 < name.length() && name.charAt(p1) == name.charAt(p1+1)){
                p1 += 1;
                p2 += 1;
                continue;
            }

            while(p2 < typed.length() && typed.charAt(p2) == name.charAt(p1)){p2 += 1;}
            p1 += 1;
        }
        if (p1 != name.length() || p2 != typed.length()){return false;}
        return true;
    }
}