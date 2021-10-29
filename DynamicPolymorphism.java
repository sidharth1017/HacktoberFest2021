class circle
{
  public void draw()
  {
    System.out.println("\r\nThe value of radius is required to draw a circle");
  }
}
class rectangle extends circle
{
public void draw()
{
System.out.println("The values of length and breadth is required to draw a circle");
}
}
class triangle extends circle
{
public void draw()
{
System.out.println("The values of sides are required to draw a circle");
}
}
class methodoverriding
{
public static void main(String args [])
{
  circle obj1=new circle();
  circle obj2=newrectangle();
  circle obj3=new triangle();
  obj1.draw();
  obj2.draw();
  obj3.draw();
}
}
