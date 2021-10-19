import java.util.*;

public class SelectionSort {
	static Scanner sc = new Scanner(System.in);
	public static void main(String args[]) {
		System.out.println("\t*****Selection Sort*****");
		long startTime,endTime;
		System.out.printf("Enter number of terms in the array: ");
		int n = sc.nextInt();
		int arr1[] = new int[n];
		int arr2[] = new int[n];
		Random r = new Random();
		for(int i=0;i<n;i++)
			arr1[i]=arr2[i] = r.nextInt(n+1);
		startTime = System.currentTimeMillis();	
		arr1 = selectionSort(arr1);	
		endTime = System.currentTimeMillis();
		System.out.println("Time required for sorting "+arr1.length+" number of elements using iterative sort is: "+((float)(endTime-startTime)/(float)1000)+" seconds"); 
		startTime = System.currentTimeMillis();
		recursiveSelectionSort(arr2,arr2.length,0);
		endTime = System.currentTimeMillis();
		System.out.println("Time required for sorting "+arr2.length+" number of elements using recursive sort is: "+((float)(endTime-startTime)/(float)1000)+" seconds");
	}
		
	
	public static int[] selectionSort(int arr[]) {
		for(int i=0;i<arr.length-1;i++) {
			int minElementIndex = i;
			for(int j=i+1;j<arr.length;j++) {
				if(arr[minElementIndex]>arr[j])
					minElementIndex = j;
			}
			int temp = arr[i];
			arr[i] = arr[minElementIndex];
			arr[minElementIndex] = temp ;
		}
		return arr;
	}
	
	public static int findMinimalElementIndex(int arr[],int i,int j) {
		// base case where recursive calls stops...
		if(i==j)
			return j;
		int index = findMinimalElementIndex(arr,i+1,j);
		if(arr[i]>arr[index])
			return index;
		else
			return i;
	}
	
	public static void recursiveSelectionSort(int arr[],int n,int i) {
		if(i==n)
			return;
		int minIndex = findMinimalElementIndex(arr, i, n-1);
		if(minIndex!=i) {
			int temp = arr[i];
			arr[i] = arr[minIndex];
			arr[minIndex] = temp;
		}
		recursiveSelectionSort(arr, n, i+1);
	}
}
