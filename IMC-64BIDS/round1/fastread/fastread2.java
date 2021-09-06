import java.io.*;
import java.util.*;
import java.lang.Math;

class Fastread2 {
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
        // skip "timestamp"
        // read timestamp number
        // skip "book"
        // read book
        // skip "bids"
        // check if need to handle bids.
        // if so, do (1), else
        // read "]"
        // then, skip "asks"
        // check if need to handle asks.
        // if so, do (1), else
        // read "]"
        //
        // (1):
        // read "{"
        // skip "price"
        // read price
        // if price is profitable (greater than or less than min/max)
        //return. else
        // skip "volume"
        // read volume
        // if finished, read "]"
        // else read ","
        // then
    }
}