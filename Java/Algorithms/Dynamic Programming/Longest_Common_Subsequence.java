
// Leetcode question no. - 1143
// Question link - https://leetcode.com/problems/longest-common-subsequence/

public class Longest_Common_Subsequence {
    class Solution {
        public int longestCommonSubsequence(String text1, String text2) {
            
            int[] prev = new int[text1.length()+1];
            int[] cur = new int[text1.length()+1];
            
            for(int i=1 ; i<=text2.length() ; i++){
                for(int j=1 ; j<=text1.length() ; j++){
                    if(text1.charAt(j-1) == text2.charAt(i-1)){
                        cur[j] = prev[j-1] + 1;
                    }
                    else{
                        cur[j] = Math.max(prev[j],cur[j-1]);
                    }
                }
                
                // prev = cur;
                System.arraycopy(cur, 0, prev, 0, text1.length() + 1);
            }
            return cur[cur.length - 1];
        }
    }
}
