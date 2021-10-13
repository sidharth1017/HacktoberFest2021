import java.text.DecimalFormat;
import java.util.Scanner;

public class SphereCalculator {

	// Method to calculate Surface area of a sphere
	public static double SurfaceAreaOfSphere(double r) {
		double surfaceArea = 4 * Math.PI * Math.pow(r, 2);
		return surfaceArea;
	}

	// Method to calculate volume of a sphere
	public static double VolumeOfASphere(double r) {
		double volume = 4 * Math.PI * Math.pow(r, 3) / 3;
		return volume;
	}

	// Method to calculate Area of a circle
	public static double AreaOfCircle(double r) {
		double area = Math.PI * Math.pow(r, 2);
		return area;
	}

	// Method to calculate circumference of a sphere
	public static double CircumferenceOfACircle(double r) {
		double circumference = 2 * Math.PI * r;
		return circumference;
	}

	// Main method
	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		DecimalFormat df = new DecimalFormat("#.###");// Create decimal formatter
		int continueCalc = 1;
		double radius;

		// Loops program
		while (continueCalc == 1) {
			System.out.print("Please enter a radius(cm):");
			radius = in.nextDouble();

			System.out.println("Radius:" + radius + "cm");

			System.out.println("Area of Sphere: " + df.format(SurfaceAreaOfSphere(radius)) + " cm^2");
			System.out.println("Volume of Sphere: " + df.format(VolumeOfASphere(radius)) + "cm^3");
			System.out.println("Area of Circle: " + df.format(AreaOfCircle(radius)) + "cm^2");
			System.out.println("Circumference of Circle: " + df.format(CircumferenceOfACircle(radius)) + "cm");

			System.out.print("Would you like to continue calculation(1=Yes 2=No):");

			try {
				continueCalc = in.nextInt();
			} catch (Exception e) {
				System.err.println("Invalid Choice!");
			}
		}
		in.close();
		System.out.println("Thank you have a nice day");
	}
}
