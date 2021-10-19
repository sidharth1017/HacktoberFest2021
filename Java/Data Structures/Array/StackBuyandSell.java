public class StackBuyandSell {
    public int buyandSell1(int[] price){
        int n=price.length;
        int maxprofit=0;;
        int minPrice=0;
        for(int i=0;i<n;i++){
            if(price[i]<minPrice){
                minPrice=price[i];
            }
            else if(price[i]-minPrice>maxprofit){
                maxprofit=price[i]-minPrice;
            }
        }
        return maxprofit;
    }
    public int buyandSell2(int[] price){
        int n=price.length;
        int ans=0;
        for(int i=1;i<n;i++){
            if(price[i]>price[i]){
                ans+=price[i]-price[i-1];
            }
        }

        return ans;
    }
    public int buyandSell3(int[] price){
        int n=price.length;
        int sell1=0;
        int buy1=Integer.MIN_VALUE;
        int sell2=0;
        int buy2=Integer.MIN_VALUE;
        for(int i=0;i<n;i++){
            sell2=Math.max( sell2 , buy2 + price[i]);
            buy2=Math.max( buy2 , sell1 - price[i]);

            sell1=Math.max( sell1 , buy1 + price[i]);
            buy1=Math.max(buy1, 0- price[i]);
        }
        return sell2;

    }
    public int buyandSellK(int[] price,int k){
        int n=price.length;
        int[][] dp=new int[k+1][price.length];
     
        for(int i=1;i<=k;i++){
            int min=-price[0];
            for(int j=1;j<n;j++){
                dp[i][j]=Math.max(dp[i][j-1],price[j]+min);
                min=Math.max(min, dp[k-1][i] - price[i]);
            }
        }
        // for(int i=0;i<n;i++){
        //     for(){

        //     }
            
        // }
        return dp[k][price.length-1];

    }
    public int buyandSellTransaction(int[] prices,int fee){
        if(prices.length==0){
            return 0;
        }
       int T_ik0=0;
        int T_ik1=Integer.MIN_VALUE;
        for(int val: prices){
            // int T_ik0old=T_ik0;
            T_ik0=Math.max(T_ik0,T_ik1+val);
            T_ik1=Math.max(T_ik1, T_ik0-val-fee);
        }
        return T_ik0;
    }
    public int buyandSellCooldown(int[] prices){
        if(prices.length==0){
            return 0;
        }
       int T_ik0=0;
        int T_ik1=Integer.MIN_VALUE;
        int T_ik0old=0;
        for(int val: prices){
            int temp=T_ik0;
            T_ik0=Math.max(T_ik0,T_ik1+val);
            T_ik1=Math.max(T_ik1, T_ik0old-val);
            T_ik0old=temp;
        }
        return T_ik0;
    }
    public static void main(String[] args) {
        int[] stockPrice=new int[]{7,1,5,3,6,4};

        StackBuyandSell a=new StackBuyandSell();
        // 1>buy and sell 1 time
        System.out.println(a.buyandSell1(stockPrice));

        //buy and sell infinite transactions but no simultaneous transactions
        System.out.println(a.buyandSell2(stockPrice));

        //buy and sell twice , one after another(2nd one only after sell of 1st one)
        System.out.println(a.buyandSell3(stockPrice));

        // k Transactions allowed
        System.out.println(a.buyandSellK(stockPrice,3));
        //buy and sell transaction fees
        System.out.println(a.buyandSellTransaction(stockPrice,4));

        // //buy and sell cooldown time (1 day cooldown)
        System.out.println(a.buyandSellCooldown(stockPrice));

    }
}
