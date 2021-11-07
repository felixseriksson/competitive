import java.io.*;
import java.util.*;

public class b {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        in.nextLine();
        int[] p = new int[n];
        for (int i = 0; i < n; i++) {
            p[i] = in.nextInt();
        }
        // System.out.println();
        // for (int i : p) {
        //     System.out.println(i);
        // }
        // System.out.println();
        in.nextLine();
        int c = 0;
        for (int i = 1; i < n+1; i++) {
            for (int j = 1; j < i; j++) {
                // System.out.println(i);
                // System.out.println(j);
                if (p[i-1] < p[j-1]) {
                    c++;
                    c %= 2;
                    // System.out.println(i);
                    // System.out.println(j);
                }
            }
        }

        int cases = in.nextInt();
        in.nextLine();
        for (int i = 0; i < cases; i++) {
            int a = in.nextInt();
            int b = in.nextInt();
            in.nextLine();
            int l = b - a;
            c += l*(l+1)/2;
            c %= 2;
            if (c == 1) {
                System.out.println("odd");
            }
            else {
                System.out.println("even");
            }
        }
    }
}