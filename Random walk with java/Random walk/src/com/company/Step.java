package com.company;

import java.util.Random;

public class Step {
    int X = 0;
    int Y = 0;
    int stepNum = 1;

    public char XYCoordinatesDist() {
        Random rand = new Random();
        int random_number = rand.nextInt(100) + 1;
        char XYvalue = ' ';
        if (random_number <= 50) {
            XYvalue = 'F';
        }
        if (random_number >= 51 && random_number <= 80) {
            XYvalue = 'L';
        }
        if (random_number >= 81) {
            XYvalue = 'R';
        }
        return XYvalue;
    }

    @Override
    public String toString() {
        return "Step number " + stepNum + " {" +
                "x=" + X +
                ", y=" + Y +
                '}';
    }
}
