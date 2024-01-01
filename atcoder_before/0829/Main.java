import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int borderMoney = scanner.nextInt();   
        int sumMoney = 0;

        int result = 0;

        for (int i = 1; i <= 10000000; i ++) {
            sumMoney += i;
            if (sumMoney >= borderMoney) {
                result = i;
                break;
            }
        }

        System.out.println(result);

        scanner.close();

    }
}


