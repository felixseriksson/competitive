import java.io.*;
import java.util.*;
import java.lang.Math;

class Flatcallsandputs {
    public static void main(String[] args) {
        List<Integer> a = List.of(549, 170, 748, 1, 341, 270, 148, 672, 882, 427);
        List<Integer> b = List.of(213, 313, 666, 896, 617, 430, 686, 135, 165, 148);
        List<Integer> c = List.of(388, 282, 539, 769, 6, 860, 733, 964, 825, 422);
        List<Integer> d = List.of(352, 476, 287, 22, 288, 327, 942, 846, 564, 324);
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
        for (int i = 1; i < (1 << ncallvolumes); i++) {
            for (int j = 1; j < (1 << nputvolumes); j++) {
                int callvolsum = 0;
                int putvolsum = 0;
                int gains = 0;
                int losses = 0;
                
                for (int calli = 0; calli < ncallvolumes; calli++) {
                    if ((i & (1 << calli)) > 0) {
                        callvolsum += callVolumes.get(calli);
                    }
                }

                for (int puti = 0; puti < nputvolumes; puti++) {
                    if ((j & (1 << puti)) > 0) {
                        putvolsum += putVolumes.get(puti);
                    }
                }
                // System.out.println(callvolsum);
                // System.out.println(putvolsum);
                // System.out.println();

                if (callvolsum == putvolsum) {
                    for (int puti = 0; puti < nputvolumes; puti++) {
                        if ((j & (1 << puti)) > 0) {
                            gains += putVolumes.get(puti)*putStrikePrices.get(puti);
                        }
                    }
                    System.out.println(gains);
                    for (int calli = 0; calli < ncallvolumes; calli++) {
                        if ((i & (1 << calli)) > 0) {
                            losses += callVolumes.get(calli)*callStrikePrices.get(calli);
                        }
                    }
                    System.out.println(losses);

                    if (gains - losses > profit) {
                        profit = gains - losses;
                    }
                }
            }
        }
        return profit;
    }
}