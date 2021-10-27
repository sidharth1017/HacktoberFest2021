import java.util.function.Function;
import java.util.*;
public class ReverseUsingFunction {
    public static void main(String args[]) {
      Function<String, String> meth = (s) -> {
          StringBuffer sb = new StringBuffer(s);
          sb.reverse();
          return sb.toString();
      };
      System.out.println(meth.apply("hello world"));
      System.out.println(meth.apply("ok hello"));
      System.out.println(meth.apply("hacktoberfest2021"));
      System.out.println(meth.apply("github"));
    }
}
//OUTPUT IS
// dlrow olleh
// olleh ko
// 1202tsefrebotkcah
// buhtig
