import java.util.*;
public class LeapYear {
    public static void main(String [] args){
   Scanner sc= new Scanner(System.in);
   int n ;
   n=sc.nextInt();
if((n%4==0 && n%100 !=0)|| n%400==0) {
    System.out.println(n+" is Leap Year");
 }
else {
    System.out.println(n+" is Not a Leap Year");
}

}
}
