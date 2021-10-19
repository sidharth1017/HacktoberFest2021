import java.util.*;
public class MajorityElementGeneral {

    public int majorityElement(int[] arr,int k){
        Arrays.sort(arr);
        int cnt=0;
        int ele=Integer.MIN_VALUE;
        for(int val:arr){
            if(val==ele){
                cnt++;
            }else{
                cnt--;
                if(cnt<=0){
                    ele=val;
                    cnt=0;
                }
            }
        }
        // System.out.println(ele);
        cnt=0;
        for(int val:arr){
            if(val==ele){
                cnt++;
            }
        }

        return cnt>=arr.length/k?cnt:-1;
    }
    public static void main(String[] args) {
        int[] arr=new int[]{3,1,2,2,1,2,3,3};
        MajorityElementGeneral o=new MajorityElementGeneral();
        System.out.println(o.majorityElement(arr,4));
        
    }
}
