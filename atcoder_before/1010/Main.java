import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        Map<Integer,ArrayList<Integer>> hashMap = new HashMap<>();


        for (int i = 1; i <= n; i++) {
            ArrayList<Integer> list = new ArrayList<>();
            hashMap.put(i, list);
        }

        // 連想配列を作成
        for (int i = 1; i <= n; i++) {
            int key = scanner.nextInt();
            int value = scanner.nextInt();
            hashMap.get(key).add(value);
            hashMap.get(value).add(key);
        }

        // ArrayList<Integer> resultList = new ArrayList<>();

        // 小さいものが一つの値をリストに追加
        // for (int i = 1; i <= top; i++) {
        //     int count = 0;
        //     for (int j = 0; j < hashMap.get(i).size(); j++) {
        //         if (i > hashMap.get(i).get(j)) {
        //             count++;
        //         }
        //     }
        //     if (count == 1) {
        //         resultList.add(i);
        //     }
        // }

        System.out.println(hashMap);

        scanner.close();

    }
}
