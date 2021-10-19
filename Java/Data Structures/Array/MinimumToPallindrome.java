public class MinimumToPallindrome {

    static int findMinOps(int[] arr, int n){
        int ans = 0; 
        for (int i=0,j=n-1; i<=j;)
        {
           
            if (arr[i] == arr[j])
            {
                i++;
                j--;
            }
            else if (arr[i] > arr[j])
            {
               
                j--;
                arr[j] += arr[j+1] ;
                ans++;
            }
            else
            {
                i++;
                arr[i] += arr[i-1];
                ans++;
            }
        }
 
        return ans;
    }
    public static void main(String[] args) {
        int arr[] = new int[]{1, 4, 5, 9, 1} ;
        System.out.println("Count of minimum operations is "+
                                findMinOps(arr, arr.length));
    }
}
