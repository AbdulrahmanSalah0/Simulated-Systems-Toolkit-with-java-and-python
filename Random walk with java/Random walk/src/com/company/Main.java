package com.company;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        char move;
        int StepsNumber;
        Step newStep = new Step();
        Scanner scn = new Scanner(System.in);
        System.out.println("Please Enter The Number Of Steps");
        StepsNumber = scn.nextInt();

        for (int step = 1; step <= StepsNumber; step++) {
            move = newStep.XYCoordinatesDist();
            if (move == 'F') {
                newStep.Y++;
            } else if (move == 'L') {
                newStep.X--;
            } else if (move == 'R') {
                newStep.X++;
            }
            System.out.println(newStep.toString());
            newStep.stepNum++;
        }
        System.out.println("\nThe Simulation End With "+StepsNumber+"  Steps" +
                "\nThe final Position is {X=" +newStep.X +",Y="+newStep.Y+"}");
    }
}