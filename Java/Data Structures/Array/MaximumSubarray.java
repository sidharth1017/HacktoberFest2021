import java.util.ArrayList;

public class MaximumSubarray {
    // 44
// {-13, 10, 6 ,16 ,-12, -4, -11, 12, 17, -19, -1, 15, 12 ,-1 ,12 ,5 ,-2 ,12 ,-17, 12, 1 ,19 ,-20 ,-14 ,12 ,-19, -9, 19, -20, 3, 5 ,-15, 3 ,-13 ,-12 ,0 ,-15 ,-16 ,-10 ,-10 ,-19, 17 ,13, 5}
    public static void main(String[] args) {
        int n=43;
        int[] arr={
        -4 ,-7 ,-6, 0 ,-19 ,2 ,-7 ,-18 ,-17, 7 ,-9 ,-1 ,8 ,19 ,-16 ,-5 
        ,3 ,8 ,5 ,11 ,14 ,17 ,-7, 11 ,-5 ,4 ,2 ,-17 ,-13 ,-19 ,-8 ,0 ,3 ,-12 ,-15 ,-13 ,-15 ,4 ,0 ,-6 ,16 ,-17 ,0};
        ArrayList<Integer> a=findSubarray(arr, n);
        for(int val:a){
            System.out.print(val+" ");
        }
    }
    public static ArrayList<Integer> findSubarray(int a[], int n) {
        // code here
        ArrayList<Integer>  temp = new ArrayList<>();
        
        
        long sum = 0;
        int startindex  = 0;
        long tempsum = 0;
        
        for(int i=0; i<a.length;i++){
            
            if(a[i]<0){
                
                if(tempsum==sum){
                    
                    if(i-startindex+1>temp.size()){
                        temp.clear();
                    
                        for(int j=startindex;j<i;j++){
                            temp.add(a[j]);
                        }
                    
                        sum = tempsum;
                    }
                }
                
                else if(tempsum>sum){
                    temp.clear();
                    
                    for(int j=startindex;j<i;j++){
                        temp.add(a[j]);
                    }
                    
                    sum = tempsum;
                }
                
                tempsum = 0;
                startindex = i+1;
            }
            
            else{
                
                tempsum += a[i];
            }
            
        }
        
        if(tempsum==sum){
                    
            if(n-startindex>temp.size()){
                temp.clear();
                    
                for(int j=startindex;j<n;j++){
                    temp.add(a[j]);
                }
                    
                sum = tempsum;
            }
        }
        
        else if(tempsum>sum){
            
            temp.clear();
            for(int j=startindex;j<n;j++){
                temp.add(a[j]);
            }
        }
        
        if(temp.isEmpty()){
            temp.add(-1);
        }
        return temp;
    }
}
