import java.util.*;
public class MergeSort {
	static Scanner sc = new Scanner(System.in);
	public static void main(String[] args) {
		System.out.println("\t\t*****MergeSort & QuickSort Algorithms*****\n");
		int c;
		System.out.printf("1)Generate Random Inputs\n2)Provide Manual Inputs\nEnter choice: ");
		c = sc.nextInt();
		int arr[];
		long start , end;
		if(c == 1) {
			arr = randomInputGenerator();
			start = System.currentTimeMillis();
			mergeSort(arr,0,arr.length-1);
			end = System.currentTimeMillis();
			System.out.println("Time required for Merge Sort for sorting "+arr.length+" elements is: "+(end-start)+" milliseconds");
		}
		
		if(c == 2) {
			arr = manualInputReader();
			start = System.currentTimeMillis();
			mergeSort(arr,0,arr.length-1);
			end = System.currentTimeMillis();
			for(int i=0;i<arr.length;i++)
				System.out.printf(arr[i]+" ");
			System.out.println();
			System.out.println("Time required for Merge Sort for sorting "+arr.length+" elements is: "+(end-start)+" milliseconds");			
		}
	}
	
	public static int[] manualInputReader() {
		System.out.printf("Enter number of terms in the array: ");
		int n = sc.nextInt();
		System.out.println("Enter input array: ");
		int arr[] = new int[n];
		for(int i=0;i<n;i++)
			arr[i] = sc.nextInt();
		return arr;
	}
	
	public static int[] randomInputGenerator() {
		System.out.printf("Enter number of terms in the array: ");
		int n = sc.nextInt();
		int arr[] = new int[n];
		Random r = new Random();
		for(int i=0;i<n;i++)
			arr[i] = r.nextInt();
		return arr;
	}

	public static void mergeSort(int arr[],int startIndex,int endIndex){
		if(startIndex<endIndex) {
			// dividing array into smaller arrays.... i.e. partitioning them into smaller sub-arrays and sorting them....
			int midIndex = (startIndex+endIndex)/2; 
			mergeSort(arr, startIndex, midIndex);
			mergeSort(arr, midIndex+1, endIndex);
			mergeArrays(arr,startIndex,midIndex,endIndex);
		}
	}
	
	public static void mergeArrays(int arr[],int s,int m,int e) {
		// length of the first array will be m/2 i.e. m-s+1
		int firstArrlen = m-s+1;
		// length of the first array will be m/2 i.e. e-m
		int secondArrlen = e-m;
		int startArray[] = new int[firstArrlen];
		int endArray[] = new int[secondArrlen];
// Creating two arrays for storing the non-merged parts.....
		for(int i=0;i<firstArrlen;i++)
			startArray[i] = arr[s+i];
		for(int j=0;j<secondArrlen;j++)
			endArray[j] = arr[m+1+j];
		int i=0,j=0,k=s;
		while(i<firstArrlen && j<secondArrlen) {
			if(startArray[i]<=endArray[j])
				arr[k++] = startArray[i++];
			else
				arr[k++] = endArray[j++];
		}
// If some elements are remaining in the array then just copy directly to the output array....
		while(i<firstArrlen)
			arr[k++] = startArray[i++];
		while(i<secondArrlen)
			arr[k++] = endArray[j++];
	}
}
