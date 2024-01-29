import java.util.Random;

public class Customer {
    int id ;
    int IAT ;
    int ST ;
    int AT ;
    int WT ;
    int timeSpend ;
    static int totalWaitingTime = 0;
    static int numOfCustomers = 0;

    String servingServer ;


    public Customer() {
        numOfCustomers++;
    }

    public int IATGenerator() {
        Random random = new Random();
        int randDegit = random.nextInt(100);
        int returnedIAT = 0;
        if (randDegit >= 0 && randDegit <= 24) {
            returnedIAT = 1;
        } else if (randDegit >= 25 && randDegit <= 64) {
            returnedIAT = 2;
        } else if (randDegit >= 65 && randDegit <= 84) {
            returnedIAT = 3;
        } else if (randDegit >= 85 && randDegit <= 99) {
            returnedIAT = 4;
        }
        return returnedIAT;
    }

    public String toString() {
        return this.id +"\t"+ this.AT +"\t"+ this.IAT +"\t"+ this.ST +"\t"+ this.WT +"\t"+ this.servingServer +"\t\t\t\t"+ this.timeSpend ;
    }

}

