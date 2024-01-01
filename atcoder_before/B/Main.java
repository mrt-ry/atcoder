package B;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int totalPerson = scanner.nextInt();        
        int totalDays = scanner.nextInt();

        List<String> personDays = new ArrayList<>();       
        
        List<Integer> enableDays = new ArrayList<>(); 

        for (int i = 0; i < totalPerson; i ++) {
            personDays.add(scanner.next());
        }

        for (int i = 0; i < totalDays - 1; i++) {
            
            for (int j = 0; j < personDays.size() - 1; j++) {
                personDays.get(j).charAt(i);
            }
        }
        scanner.close();
    }
}

