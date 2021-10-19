public class firstMissingPositive {
    public static void main(String[] args) {
        int[] nums={1,-10,2,3,-20};
        int i=0;
        while(i<nums.length){   
            if (nums[i] == i+1 || nums[i] <= 0 || nums[i] > nums.length                   || nums[nums[i] - 1] == nums[i]) {
                i++;
            } else {
                swap(nums, i, nums[i] - 1);
            }
        }
       i = 0; 
        while(i < nums.length && nums[i] == i+1) i++;
        System.out.println( i+1);
    }
    
    private static void swap(int[] arr,int i,int j ){
        int temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
        return;
    }
}
