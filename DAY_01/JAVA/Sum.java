// take input store n and find sum till n*/

import java.util.*;
public class Sum{
    public static void main(String[] args){
        Scanner sc= new Scanner(System.in);
        int n=sc.nextInt();
        int i=0,sum=0;
        while(i<=n){
            sum+=i;
            i++;
        }
        System.out.println(sum);
    }
}