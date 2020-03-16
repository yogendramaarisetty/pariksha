//NOTE: Don't change class name
import java.util.*;
public class MyClass {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int a[] = new int[n];
        for(int i=0;i<n;i++){
            a[i] = sc.nextInt();
        }
        int t = sc.nextInt();
        int r1=0,r2=0;
        for(int i=0;i<n-1;i++){
            int diff = t - a[i];
            for(int j=i+1;j<n;j++){
                if(a[j] == diff){
                    r1 = i;
                    r2 = j;
                    break;
                }
            }
        }
      System.out.println(r1+" "+r2);
    }
}
