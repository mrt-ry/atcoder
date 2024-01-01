import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int result = 0;

        while(true) {
            int hundred = n / 100;
            int ten = (n - hundred * 100) / 10;
            int one = (n - ten * 10) % 10;
            if (hundred * ten == one) {
                result = n;
                break;
            }
            n++;
        }


        System.out.println(result);

        scanner.close();

    }
}
