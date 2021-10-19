public class MinimumMemory {
    public static void main(String[] args) {
        int[] arr={41,67,70,55,53,23,69};
        int ans=0;
        for(int val:arr){
            ans+=val;
        }
        System.out.println(ans);
    }
}
