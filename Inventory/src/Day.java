import java.util.Random;

public class Day {
    int dayNum;
    int cycleNum;
    int invBegin;
    int demand;
    int invEnd;
    int shortage;
    int order;
    int leadTime = -1;
    static int activeOrder;
    static int shortagePerCycle;

    @Override
    public String toString() {
        return "dayNum = " + dayNum +
                ", cycleNum = " + cycleNum +
                ", invBegin = " + invBegin +
                ", demand = " + demand +
                ", invEnd = " + invEnd +
                ", shortage = " + shortage +
                ", order = " + order +
                ", leadTime = " + leadTime;
    }

    public static int demand() {
        Random rand = new Random();
        int random_number = rand.nextInt(100);
        int demandValue = 0;
        if (random_number >= 0 && random_number <= 9) {
            demandValue = 0;
        }
        if (random_number >= 10 && random_number <= 34) {
            demandValue = 1;
        }
        if (random_number >= 35 && random_number <= 69) {
            demandValue = 2;
        }
        if (random_number >= 70 && random_number <= 90) {
            demandValue = 3;
        }
        if (random_number >= 91 && random_number <= 99) {
            demandValue = 4;
        }
        return demandValue;
    }

    public static int leadTime() {
        Random rand = new Random();
        int randomNumber = rand.nextInt(10);
        int leadTimeValue = 0;
        if (randomNumber >= 0 && randomNumber <= 5) {
            leadTimeValue = 1;
        }
        if (randomNumber >= 6 && randomNumber <= 8) {
            leadTimeValue = 2;
        }
        if (randomNumber == 9) {
            leadTimeValue = 3;
        }
        return leadTimeValue;
    }
}
