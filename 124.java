/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val; 
 *     TreeNode left; 
 *     TreeNode right; 
 *     TreeNode() {} 
 *     TreeNode(int val) { this.val = val; } 
 *     TreeNode(int val, TreeNode left, TreeNode right) { 
 *         this.val = val; 
 *         this.left = left; 
 *         this.right = right; 
 *     }
 * }
 */

class Solution {
    public int res = -10000;
    public int maxPathSum(TreeNode root) {
        // only one seperation, as root
        // backtracking, return maximum of left path or right path
        // if negative, then no need to sum it
        helper(root);
        return res;
    }

    public int helper(TreeNode root) {
        if (root == null){return 0;}
        int left = helper(root.left);
        int right = helper(root.right);
        res = Math.max(res,left + right + root.val);
        return Math.max(0,root.val + Math.max(left,right));
    }
}