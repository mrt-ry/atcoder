package B;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        

        int numTotal = scanner.nextInt();

        int ansNum = 0;


        List<Integer> numList = new ArrayList<>();          
        List<Integer> ascNumList = new ArrayList<>();       
     

        for (int i = 0; i < numTotal; i ++) {
            numList.add(scanner.nextInt());
        }


        int minValue = 1000;        
        int maxValue= 0;

        for (int i = 0; i < numTotal; i++) {
            if (minValue > numList.get(i)) {
                minValue = numList.get(i);
            }
            if (maxValue < numList.get(i)) {
                maxValue = numList.get(i);
            }
        } 

        for (int i = minValue; i <= maxValue; i++) {
            ascNumList.add(i);
        }
    

        for (int i = 0; i < maxValue - minValue + 1; i++) {
            if (!numList.contains(ascNumList.get(i))) {
                ansNum = ascNumList.get(i);
            }
        }

        System.out.println(ansNum);




        scanner.close();

    }
}


