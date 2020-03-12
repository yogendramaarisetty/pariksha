import java.io.*;
import java.util.*;


public class MyClass {
    public static void main(String args[] ) throws Exception {
        boolean [] a = new boolean[200];
        Arrays.fill(a,true);
        for(int i =2 ;i<Math.sqrt(200);i++){
            if(a[i]){
                for(int j =2;j<200;j++){
                    if(i*j>=200){
                        break;
                    }
                    a[i*j]= false;
                    
                }
            }
        }
        for(int i =4 ;i<65;i++){
            a[i]=false;
        }
        for(int i =91;i<97;i++){
            a[i]=false;
        }
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while(t--!=0){
            int l = Integer.parseInt(br.readLine());
            String  s = br.readLine();
            //  System.out.println(s);
            String r = "";
            for(int i =0; i< l ;i++){
                if(!a[(int)s.charAt(i)]){
                   r+= nearestPrime((int)s.charAt(i),a);
                }
                else{
                    r+=Character.toString(s.charAt(i));
                }
            }
            System.out.println(r);
        }
        

    }
    static String nearestPrime(int p,boolean [] a) throws ArrayIndexOutOfBoundsException{
        int i =p,j=p;
        
        while(!a[i] && i<127){
            i++;
        }
        while(!a[j]&& j>0){
            j--;
        }
        int u = i-p;
        int v=p-j;
        if(i>122){
            return Character.toString((char)j);
        }
        else if(j<65){
            return Character.toString((char)i);
        }
       return u<v ? Character.toString((char)i):  Character.toString((char)j);
        
    }
    
}

