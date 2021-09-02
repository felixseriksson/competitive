import java.io.*;

class Timevalue {
    public static void main(String[] args) {
        double time = calculateTime(365, 0, 1);
        System.out.println(time);
    }

    static double calculateTime(int days, int hours, int minutes) {
        return (double) ((double) days / 365) + ((double) hours / (365*24)) + ((double) minutes / (365*24*60));
    }
}