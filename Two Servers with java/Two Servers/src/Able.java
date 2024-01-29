import java.util.Random;

public class Able {
    int AbleST;
    int state = 0;
    int currentST;
    int totalServiceTime;

    public int AbleSTGenerator() {
        Random random = new Random();
        int randDegit = random.nextInt(100);
        if (randDegit >= 0 && randDegit <= 29) {
            AbleST = 2;
        } else if (randDegit >= 30 && randDegit <= 57) {
            AbleST = 3;
        } else if (randDegit >= 58 && randDegit <= 82) {
            AbleST = 4;
        } else if (randDegit >= 83 && randDegit <= 99) {
            AbleST = 5;
        }
        return AbleST;
    }
}
