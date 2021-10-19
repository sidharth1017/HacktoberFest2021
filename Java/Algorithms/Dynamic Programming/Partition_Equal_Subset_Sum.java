
// Leetcode question no. - 416
// Question link - https://leetcode.com/problems/partition-equal-subset-sum/

public class Partition_Equal_Subset_Sum {
    class Solution {
        public boolean canPartition(int[] nums) {
         
            int sum = 0;
            
            for(int i=0 ; i<nums.length ; i++){
                sum += nums[i];
            }
            
            if(sum%2 != 0){
                return false;
            }
            else if(subsetSum(nums,sum/2,nums.length)){
                return true;
            }
            else{
                return false;
            }
        }
        
        public boolean subsetSum(int[] a,int sum,int n){
            boolean[][] dp = new boolean[n+1][sum+1];
            
            dp[0][0] = true;
            
            for(int i=1 ; i<=n ; i++){
                for(int j=0 ; j<=sum ; j++){
                    if(j == 0){
                        dp[i][j] = true;
                    }
                    else if(a[i-1] <= j){
                        dp[i][j] = dp[i-1][j - a[i-1]] || dp[i-1][j];
                    }
                    else{
                        dp[i][j] = dp[i-1][j];
                    }
                }
            }
            return dp[n][sum];
        }
    }
}
