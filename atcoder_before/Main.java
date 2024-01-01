import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int dayN = scanner.nextInt();
        int firstDay = scanner.nextInt();
        int increaseDay = scanner.nextInt();

        int count = 0;

        for (int i = firstDay; i <= dayN; i+=increaseDay) {
            count++;
        }

        System.out.println(count);
        scanner.close();
    }
}