class Solution {
    public int maxUncrossedLines(int[] nums1, int[] nums2) {
        int [][] dp = new int[nums1.length][nums2.length];
        for (int i = 0;i<nums1.length;i++){
            for (int j = 0;j<nums2.length;j++){
                if(nums1[i]==nums2[j]){if(i==0||j==0){dp[i][j]=1;}
                else{dp[i][j]=dp[i-1][j-1]+1;}
                }
                else{
                    if(i==0&&j==0){dp[i][j]=0;}
                    else if(i==0&&j!=0){dp[i][j]=dp[i][j-1];}
                    else if(i!=0&&j==0){dp[i][j]=dp[i-1][j];}
                    else{dp[i][j]=Math.max(dp[i-1][j],dp[i][j-1]);}
                }
            }
        }
        return dp[nums1.length-1][nums2.length-1];
    }
}

// simpler space complexity
class Solution2 {
    public int maxUncrossedLines(int[] nums1, int[] nums2) {
        int [][] dp = new int[2][nums2.length];
        for (int i = 0;i<nums1.length;i++){
            int k = i % 2;
            for (int j = 0;j<nums2.length;j++){
                if(nums1[i]==nums2[j]){if(i==0||j==0){dp[k][j]=1;}
                else{dp[k][j]=dp[(k+1)%2][j-1]+1;}
                }
                else{
                    if(i==0&&j==0){dp[i][j]=0;}
                    else if(i==0&&j!=0){dp[i][j]=dp[i][j-1];}
                    else if(i!=0&&j==0){dp[k][j]=dp[(k+1)%2][j];}
                    else{dp[k][j]=Math.max(dp[(k+1)%2][j],dp[k][j-1]);}
                }
            }
        }
        return dp[(nums1.length-1)%2][nums2.length-1];
    }
}
