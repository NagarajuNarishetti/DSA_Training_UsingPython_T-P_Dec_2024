import java.util.*;
public class EvenOdd {
    public static void main(String [] args){
    Scanner sc= new Scanner(System.in);
        int n;
        n=sc.nextInt();
        if((n&1)==1){
            System.out.println("Odd");
        }
        else {
            System.out.println("Even");
        }
    }
}
