import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int a = scanner.nextInt();
        int b = scanner.nextInt();

        int result;

        result = (int)Math.pow(a, b) + (int)Math.pow(b, a);

        System.out.println(result);

        scanner.close();

    }
}




