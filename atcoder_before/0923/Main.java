import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int num = scanner.nextInt();

        List<Integer> list = new ArrayList<>();
        while(num != 0) {
            list.add(num % 10);
            num /= 10;
        }

        Collections.reverse(list);        Collections.reverse(list);


        String result = "Yes"; 

        int targetNum = 100000000;
        for (int i = 0; i < list.size(); i++) {
            if (targetNum  <= list.get(i)) {
                result = "No";
                break;
            }
            targetNum = list.get(i);
        }


        System.out.println(result);

        scanner.close();

    }
}