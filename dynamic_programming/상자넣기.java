package dynamic_programming;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 상자넣기 {

    static int n;
    static int[] boxes;

    public static void main(String[] args) throws Exception{

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(bf.readLine());
        boxes = Arrays.stream(bf.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        System.out.println(dp());
    }

    private static int dp() {

        int[] memory = new int[n];

        for(int i=0; i<n; i++) {
            for (int j=i+1; j<n; j++) {
                if (boxes[i] < boxes[j]) {
                    memory[j]++;
                }
            }
        }
        for (int i : memory) {
            System.out.println(i);
        }

        return Arrays.stream(memory).max().getAsInt();
    }
}
