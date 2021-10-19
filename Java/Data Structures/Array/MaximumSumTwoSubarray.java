

public class MaximumSumTwoSubarray {
    public static void main(String[] args) {
        int[] A=new int[]{};
        int L=1;
        int M=2;
        for (int i = 1; i < A.length; ++i)
            A[i] += A[i - 1];
        int res = A[L + M - 1], Lmax = A[L - 1], Mmax = A[M - 1];
        for (int i = L + M; i < A.length; ++i) {
            Lmax = Math.max(Lmax, A[i - M] - A[i - L - M]);
            Mmax = Math.max(Mmax, A[i - L] - A[i - L - M]);
            res = Math.max(res, Math.max(Lmax + A[i] - A[i - M], Mmax + A[i] - A[i - L]));
        }
        System.out.println(res);;
        
    }
}
