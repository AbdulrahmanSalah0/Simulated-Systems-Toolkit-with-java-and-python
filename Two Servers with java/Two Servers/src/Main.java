import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) {
        Able Able = new Able();
        Baker Baker = new Baker();
        Queue<Customer> customersQ = new LinkedList<Customer>();
        ArrayList<Customer> customersInfo = new ArrayList<Customer>();
        int AtNext = 0;
        int IDNext = 1;
        int IATNext = 0;
        int WTNext = 0 ;
        int TotalServiceTimeForTwoServers = 0 ;
        int TheTotalWT = 0 ;
        int numOfCustomersWaited = 0;
        for (int min = 0; min <= 59; min++) {
            if (AtNext == min) {
                Customer newCustomer = new Customer();
                newCustomer.id = IDNext;
                newCustomer.AT = AtNext;
                newCustomer.IAT = IATNext;
                customersQ.add(newCustomer);
                IATNext = newCustomer.IATGenerator();
                AtNext = (IATNext) + AtNext;
                IDNext++;
            }
            if (Baker.state == 0) {
                if (customersQ.peek() != null) {

                    Customer removedFromQ = new Customer();
                    Baker.state = 1;
                    removedFromQ = customersQ.poll();
                    removedFromQ.ST = Baker.BakerSTGenerator();
                    removedFromQ.WT = min - removedFromQ.AT ;
                    removedFromQ.timeSpend = removedFromQ.ST + removedFromQ.WT ;
                    removedFromQ.servingServer = "Baker";
                    Baker.currentST = removedFromQ.ST;
                    Baker.totalServiceTime = Baker.totalServiceTime + removedFromQ.ST;
                    customersInfo.add(removedFromQ);
                }
            } else {
                Baker.currentST--;
                if (Baker.currentST == 1) {
                    Baker.state = 0;
                }
            }
            if (Able.state == 0) {
                if (customersQ.peek() != null) {
                    Customer removedFromQ = new Customer();
                    Able.state = 1;
                    removedFromQ = customersQ.poll();
                    removedFromQ.ST = Able.AbleSTGenerator();
                    removedFromQ.WT = min - removedFromQ.AT ;
                    removedFromQ.timeSpend = removedFromQ.ST + removedFromQ.WT ;
                    removedFromQ.servingServer = "Able";
                    Able.currentST = removedFromQ.ST;
                    Able.totalServiceTime = Able.totalServiceTime + removedFromQ.ST;
                    customersInfo.add(removedFromQ);
                }
            } else {
                Able.currentST--;
                if (Able.currentST == 1) {
                    Able.state = 0;
                }
            }
        }
        TotalServiceTimeForTwoServers = Able.totalServiceTime + Baker.totalServiceTime ;
        for (int i = 0 ; i < customersInfo.size(); i++){
            TheTotalWT = TheTotalWT + customersInfo.get(i).WT ;
        }
        for (int i = 0 ; i < customersInfo.size(); i++){
            if (customersInfo.get(i).WT != 0){
                numOfCustomersWaited = numOfCustomersWaited + 1 ;
            }
        }
        System.out.println("id" + "\t" + "AT" + "\t" + "IAT" + "\t" + "ST" + "\t" + "WT" + "\t" + "ServingServer" + "\t" + "Time spend");
        for (int i = 0; i < customersInfo.size(); i++) {
            System.out.println(customersInfo.get(i));
        }
        System.out.println("\n");
        System.out.println("Able busy time percentage to the total time = " + ((double) Able.totalServiceTime / 60) * 100 + "%");
        System.out.println("Average waiting time of all  customers = " + ((double) TheTotalWT) / numOfCustomersWaited);
        System.out.println("Total service time for both servers = " + TotalServiceTimeForTwoServers );
        System.out.println("Total waiting time of all customers ="+ TheTotalWT);
        System.out.println("Able's total service time = " + Able.totalServiceTime);
        System.out.println("Baker's total service time = " + Baker.totalServiceTime);
    }

}

