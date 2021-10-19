import java.util.Scanner;

public class profitGain {
    public static void main(String[] args) {
        try{
            Scanner scn=new Scanner(System.in);
            int n=scn.nextInt();
            int[] arr=new int[n];
            for(int i=0;i<n;i++){
                arr[i]=scn.nextInt();
            }
            int[] dp=new int[n];
            long max=0;
            dp[0]=arr[0];
            for(int i=1;i<n;i++){
                dp[i]=arr[i];
                
                for(int j=0;j<i;j++){
                    if((arr[i]%arr[j])==0){
                        dp[i]=Math.max(dp[i],dp[j]+arr[i]);
                    }
                }
                max=Math.max(max,dp[i]);
            }
            System.out.println(max);
            scn.close();
        }catch(Exception e){

        }     
   }
}
