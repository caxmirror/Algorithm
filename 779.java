class Solution {
    public int kthGrammar(int n, int k) {
        if (n==1){return 0;}
        System.out.println(n+" "+k);
        if (n == 2){
            if(k==1){return 0;}
            else {return 1;}
        }
        if ((k - (int)Math.pow(2,n-2)) > 0){
            k = k - (int)Math.pow(2,n-2);
            if (kthGrammar(n-1, k) == 0)
            {return 1;}
            else {return 0;}
        }
        else{
            return (kthGrammar(n-1, k));
        }
    }
}