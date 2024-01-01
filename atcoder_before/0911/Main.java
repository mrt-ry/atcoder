import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int cityNums = scanner.nextInt();
        int wayNums = scanner.nextInt();
        Map<Integer,ArrayList<Integer>> hashMap = new HashMap<>();


        for (int i = 1; i <= cityNums; i++) {
            ArrayList<Integer> list = new ArrayList<>();
            hashMap.put(i, list);
        }
  

        for (int i = 1; i <= wayNums; i++) {
            // String values = scanner.nextLine();
            int key = scanner.nextInt();
            int value = scanner.nextInt();
            hashMap.get(key).add(value);
            hashMap.get(value).add(key);
        }
   

        // キーでソート
        Object[] keyArray = hashMap.keySet().toArray();
        Arrays.sort(keyArray);

        // 配列をソートして表示
        for (int i = 1; i <= cityNums; i++) {
            Collections.sort(hashMap.get(i));
            System.out.print(hashMap.get(i).size() + " ");
            for (int n = 0; n < hashMap.get(i).size(); n++ ) {
                System.out.print(hashMap.get(i).get(n) + " ");
            }
            System.out.println("");
        }

        scanner.close();

    }
}


