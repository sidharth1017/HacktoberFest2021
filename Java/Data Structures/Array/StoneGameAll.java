public class StoneGameAll {
    
    public static void main(String[] args) {
        // StoneGameAll a=new StoneGameAll();
        Solution b=new Solution();
        int[] piles=new int[]{};
        //choices First and Last
        System.out.println(b.StoneGame1(piles));
        //Choices 1st - 2M and then choices changes from Math.max(x,m) x being what you chose last;
    }
}
class Solution{

    public boolean StoneGame1(int[] piles){
        if(piles.length==2){
            return true;
        }
        int totalStones=0;
        for(int pile:piles){
            totalStones+=pile;
        }
        int n=piles.length;
      
        int ans=recurStoneGame(piles,0,n-1,new int[n][n],true);
        return ans*2>totalStones;
    }
    private int recurStoneGame(int[] piles,int st,int end,int[][] dp,boolean turn){
        if(st>end){
            return 0;
        }
        if(dp[st][end]>0){
            return dp[st][end];
        }
       
        if(turn){
            int alexSt1=recurStoneGame(piles,st+2,end-1,dp,false)+piles[st];
            int alexEnd2=recurStoneGame(piles,st,end-2,dp,false)+piles[end];
            dp[st][end]=Math.max(alexSt1,alexEnd2);
            return dp[st][end];
        }else{
            int alexSt2=recurStoneGame(piles,st+1,end-2,dp,true)+piles[st];
        
            int alexEnd1=recurStoneGame(piles,st+1,end-1,dp,true)+piles[end];

           
            dp[st][end]=Math.max(alexSt2,alexEnd1);
            return  dp[st][end];
        }
        
        
        
    }

    public String stoneGameIII(int[] stoneValue) {
        int n = stoneValue.length, dp[] = new int[n+1];
        for (int i = n - 1; i >= 0; --i) {
            dp[i] = Integer.MIN_VALUE;
            for (int k = 0, take = 0; k < 3 && i + k < n; ++k) {
                take += stoneValue[i + k];
                dp[i] = Math.max(dp[i], take - dp[i + k + 1]);
            }
        }
        if (dp[0] > 0) return "Alice";
        if (dp[0] < 0) return "Bob";
        return "Tie";
    }

    public boolean winnerSquareGame(int n) {
        boolean[] dp=new boolean[n+1];
        for(int i=1;i<=n;++i){
            for(int k=1;k*k<=i;++k){
                if( !dp[i-k*k]){
                    dp[i]=true;
                    break;
                }
            }
        }
        return dp[n];
    }
}
