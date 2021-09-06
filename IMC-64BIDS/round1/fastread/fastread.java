import java.io.*;
import java.util.*;
import java.lang.Math;

class Fastread {
    public static void main(String[] args) {
        double buyprice = 700;
        double sellprice = 900;
        // String state = "{\"timestamp\":0,\"book\":\"AAPL\",\"bids\":[{\"price\":100,\"volume\":10}],\"asks\":[{\"price\":600,\"volume\":10}]}";
        String state = "{\"timestamp\":0,\"book\":\"AAPL\",\"bids\":[],\"asks\":[{\"price\":600,\"volume\":10}]}";
        // double buyprice = 500;
        // double sellprice = 900;
        // String state = "{\"timestamp\":15,\"book\":\"TSLA\",\"bids\":[{\"price\":800,\"volume\":50},{\"price\":850,\"volume\":110}],\"asks\":[]}";
        System.out.println(fastRead(buyprice, sellprice, state));
    }

    static String fastRead(double maxBuyPrice, double minSellPrice, String marketState) {
        String actions = "";
        actions = actions.concat("S13 ");
        int i = 13;
        
        int counter = 0;
        while (Character.isDigit(marketState.charAt(i))) {
            i++;
            counter++;
        }
        i++;
        counter++;
        actions = actions.concat("R" + Integer.toString(counter) + " ");

        actions = actions.concat("S8 ");
        i += 8;

        counter = 0;
        while (Character.isLetter(marketState.charAt(i)) || marketState.charAt(i) == '_') {
            i++;
            counter++;
        }
        i++;
        counter++;
        actions = actions.concat("R" + Integer.toString(counter) + " ");

        actions = actions.concat("S9 ");
        i += 9;

        Boolean first = true;
        while (marketState.charAt(i) != ']') {
            // System.out.println(marketState.charAt(i));
            if (first) {
                actions = actions.concat("R1 ");
                i++;
            }
            actions = actions.concat("S8 ");
            i+=8;
            String num = "";
            counter = 0;
            while (Character.isDigit(marketState.charAt(i))) {
                num = num.concat(String.valueOf(marketState.charAt(i)));
                i++;
                counter++;
            }
            i++;
            counter++;

            actions = actions.concat("R" + Integer.toString(counter) + " ");

            // System.out.println("He");
            // System.out.println(num);
            int price = Integer.parseInt(num);

            if (price >= minSellPrice) {
                return actions;
            }
            else {
                // Hantera inläsning av "volume", den faktiska volymen
                // samt kolla om vi är klara med bids eller om vi ska upprepa.
                first = false;
                actions = actions.concat("S9 ");
                i += 9;

                counter = 0;
                while (marketState.charAt(i) != '}') {
                    i++;
                    counter++;
                }
                i++;
                counter++;
                actions = actions.concat("R" + Integer.toString(counter) + " ");

                if (marketState.charAt(i) == ',') {
                    i++;
                    actions = actions.concat("R1 ");
                    i++;
                    actions = actions.concat("S1 ");
                }
            }
        }

        actions = actions.concat("R1 ");
        i++;

        actions = actions.concat("S9 ");
        i += 9;

        first = true;
        while (marketState.charAt(i) != ']') {
            if (first) {
                actions = actions.concat("R1 ");
                i++;
            }
            actions = actions.concat("S8 ");
            i+=8;
            String num = "";
            counter = 0;
            while (Character.isDigit(marketState.charAt(i))) {
                num = num.concat(String.valueOf(marketState.charAt(i)));
                i++;
                counter++;
            }
            i++;
            counter++;

            actions = actions.concat("R" + Integer.toString(counter) + " ");
            
            int price = Integer.parseInt(num);

            if (price <= maxBuyPrice) {
                return actions;
            }
            else {
                // Hantera inläsning av "volume", den faktiska volymen
                // samt kolla om vi är klara med bids eller om vi ska upprepa.
                first = false;
                actions = actions.concat("S9 ");
                i += 9;

                counter = 0;
                while (marketState.charAt(i) != '}') {
                    i++;
                    counter++;
                }
                i++;
                counter++;
                
                if (marketState.charAt(i) == ',') {
                    i++;
                    actions = actions.concat("R1 ");
                    i++;
                    actions = actions.concat("S1 ");
                }
                
            }
        }

        actions = actions.concat("R1 ");
        i++;
        return actions;
    }
}