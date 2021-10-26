import java.util.*;
class zeller
{
    public static void main(String args[])
    {
        Scanner I=new Scanner(System.in);
        int i,d,m,y,s=0,M=0,D,C;
        String x, h = "",c = "";
        String a[]={"SUNDAY","MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY"};    //Arrays for the day
        System.out.println("ENTER THE DATE");
        d=I.nextInt();

        System.out.println("ENTER THE MONTH");
        m=I.nextInt();

        System.out.println("ENTER THE YEAR");
        y=I.nextInt();

        if((y<0||m<1||d<1||d>31||m>12)||(y%4!=0&&m==2&&d>28)||(m!=8&&m%2==0&&d>30))
           System.out.println("INVALID ENTRY");
        else
         {
             c=Integer.toString(y);
             for(i=c.length();i<4;i++)
              c = "0" + c;
             D=Integer.parseInt(c.substring(2));
             C=Integer.parseInt(c.substring(0,2));

             if(C == 0 && D == 1)
               {
                   D=D+6;
                   C=C+1;
               }

             if(m > 2)
              M = m - 2;
             else
              D = D - 1;

             if(m <= 2)
               M = 12- m%2;
             s = d + ((13 * M) - 1)/5 + D + (D/4) + (C/4) - (2 * C);

             if(s<0)
               s = s + 7;

             if(m < 10)
               h = "0" + Integer.toString(m);

             System.out.println("Date you entered:" + d+"//" +h+"//"+ c+"\nIT WAS:"+a[s%7]);  
            }   
        }
    }
