public class numberSubarraysMaximumValueGivenRange {

    static long countSubarrys(long n){
        return n * (n + 1) / 2;
    }

    static long countSubarrays(int a[], int n,int L, int R){
        long res = 0;
    
        long exc = 0, inc = 0;
    
        for (int i = 0; i < n; i++) {
            if (a[i] > R) {
                res += (countSubarrys(inc) - countSubarrys(exc));
                inc = 0;
                exc = 0;
            }
        
            else if (a[i] < L) {
                exc++;
                inc++;
            }
            else {
                res -= countSubarrys(exc);
                exc = 0;
                inc++;
            }
        }
    
        res += (countSubarrys(inc) - countSubarrys(exc));
    
        return res;
    }
    public static void main(String[] args) {
        int a[] = {2, 0, 11, 3, 0};
        int n = a.length;
        int l = 1, r = 10;
        System.out.print(countSubarrays(a, n, l, r));
    }   
}
