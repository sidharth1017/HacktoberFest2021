
// Leetcode question no. - 494
// Question link - https://leetcode.com/problems/target-sum/


public class Target_Sum {
    class Solution {
        public int findTargetSumWays(int[] a, int diff) {
            
            int sum = 0;
            int n = a.length;
    
            for(int i=0 ; i<n ; i++){
                sum += a[i];
            }
    
            int s1 = (diff + sum)/2;
    
            if(diff > sum || (diff+sum)%2 != 0){
                return 0;
            }
            else{
                return countOfSubsets(a,n,s1);
            }
        }
    
        public int countOfSubsets(int[] a,int n,int sum){
    
           int[][] dp = new int[n+1][sum+1];
    
            dp[0][0] = 1;
    
            for(int i=1 ; i<=n ; i++){
                for(int j=0 ; j<=sum ; j++){
                    if(j == 0){
                        if(a[i-1] == 0){
                            dp[i][j] = dp[i-1][j]*2;
                        }
                        else{
                            dp[i][j] = dp[i-1][j];
                        }
                    }
                    else if(a[i-1] <= j){
                        dp[i][j] = dp[i-1][j - a[i-1]] + dp[i-1][j];
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
