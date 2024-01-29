import java.util.Random;

public class Baker {
    int BakerST;
    int state;
    int currentST;
    int totalServiceTime;
    public int BakerSTGenerator() {
        Random random = new Random();
        int randDegit = random.nextInt(100);
        if (randDegit >= 0 && randDegit <= 34) {
            BakerST = 2;
        } else if (randDegit >= 35 && randDegit <= 59) {
            BakerST = 3;
        } else if (randDegit >= 60 && randDegit <= 79) {
            BakerST = 4;
        } else if (randDegit >= 80 && randDegit <= 99) {
            BakerST = 5;
        }
        return BakerST;
    }

}
