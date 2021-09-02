import java.io.*;
import java.util.*;
import java.lang.Math;

class Flatcallsandputs {
    public static void main(String[] args) {
        List<Integer> a = List.of(3, 9, 7);
        List<Integer> b = List.of(1, 3, 2);
        List<Integer> c = List.of(10, 10);
        List<Integer> d = List.of(2, 2);
        int profit = calculateProfit(a, b, c, d);
        System.out.println(profit);
        // for (int bit = 0; bit < 10; bit++) {
        //     System.out.println(getBit((1 << 10) - 1, bit));
        // }
    }

    static int calculateProfit(List<Integer> callStrikePrices, List<Integer> callVolumes, List<Integer> putStrikePrices, List<Integer> putVolumes) {
        int ncallvolumes = callVolumes.size();
        int nputvolumes = putVolumes.size();
        int profit = 0;
        for (int i = 0; i < (1 << ncallvolumes); i++) {
            for (int j = 0; j < (1 << nputvolumes); j++) {
                int callvolsum = 0;
                int putvolsum = 0;
                for (int iindex = ncallvolumes; iindex > 0; iindex-- ) {
                    // System.out.println("Trying to get index " + String.valueOf(ncallvolumes-iindex));
                    callvolsum += getBit(i, iindex)*callVolumes.get(ncallvolumes-iindex);
                }
                // System.out.println("Finished first indexing");
                for (int jindex = nputvolumes; jindex > 0; jindex-- ) {
                    // System.out.println("Trying to get index " + String.valueOf(nputvolumes-jindex));
                    putvolsum += getBit(j, jindex)*putVolumes.get(nputvolumes-jindex);
                }
                // System.out.println("Finished second indexing");
                if (callvolsum == putvolsum) {
                    int potentialloss = 0;
                    int potentialgain = 0;
                    for (int iindex = ncallvolumes; iindex > 0; iindex-- ) {
                        // System.out.println("Adding callval at index " + String.valueOf(ncallvolumes-iindex));
                        potentialloss += getBit(i, iindex)*callVolumes.get(ncallvolumes-iindex)*callStrikePrices.get(ncallvolumes-iindex);
                    }
                    // System.out.println("Finished third indexing");
                    for (int jindex = nputvolumes; jindex > 0; jindex-- ) {
                        // System.out.println("Adding putval at index " + String.valueOf(nputvolumes-jindex));
                        potentialgain += getBit(j, jindex)*putVolumes.get(nputvolumes-jindex)*putStrikePrices.get(nputvolumes-jindex);
                    }
                    // System.out.println("Finished fourth indexing");
                    System.out.println("Current i: " + String.valueOf(i));
                    System.out.println("Current j: " + String.valueOf(j));
                    int potentialprofit = potentialgain - potentialloss;
                    System.out.println(potentialprofit);
                    profit = (potentialprofit > profit) ? potentialprofit : profit;
                }
            }
        }
        return profit;
    }

    static int getBit(int n, int k) {
        return (n >> k) & 1;
    }
}