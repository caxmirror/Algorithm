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
    public int rangeSumBST(TreeNode root, int low, int high) {
        Stack<TreeNode> stack = new Stack<>();
        int res = 0;
        stack.push(root);
        while (stack.size()!=0){
            TreeNode node = stack.pop();
            if (node.val>=low && node.val<=high){
                res += node.val;
            }
            if(node.left != null){stack.push(node.left);}
            if(node.right != null){stack.push(node.right);}
        }
        return res;
    }
}