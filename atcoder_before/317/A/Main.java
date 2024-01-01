import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int medicineNums = scanner.nextInt();
        int monsterHp = scanner.nextInt();
        int borderHp = scanner.nextInt(); 

        int resultMedicine = 0;

        List<Integer> increaseHp = new ArrayList<>();       

        for (int i = 0; i < medicineNums; i ++) {
            increaseHp.add(scanner.nextInt());
        }

        for (int i = 0; i < medicineNums; i++) {
            if (increaseHp.get(i) + monsterHp >= borderHp) {
                resultMedicine = i;
                break;
            }
        }
        System.out.println(resultMedicine + 1);
        scanner.close();

    }
}


