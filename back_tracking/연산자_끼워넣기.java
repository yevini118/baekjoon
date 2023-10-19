package back_tracking;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.SQLOutput;
import java.util.Arrays;

public class 연산자_끼워넣기 {

    static int N;
    static int[] nums;
    static int[] operations;
    static int min = Integer.MAX_VALUE;
    static int max = Integer.MIN_VALUE;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        nums = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        operations = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        back(1, nums[0]);

        System.out.println(max);
        System.out.println(min);
    }

    private static void back(int numIdx, int result) {

        if (numIdx == N) {
            min = Math.min(min, result);
            max = Math.max(max, result);
            return;
        }

        for (int i=0; i<4; i++) {

            if (operations[i] > 0) {

                operations[i] --;

                switch(i) {
                    case 0:
                        back(numIdx+1, result + nums[numIdx]);
                        break;
                    case 1:
                        back(numIdx+1, result - nums[numIdx]);
                        break;
                    case 2:
                        back(numIdx+1, result * nums[numIdx]);
                        break;
                    case 3:
                        back(numIdx+1, result / nums[numIdx]);
                        break;
                }
                operations[i] ++;
            }
        }

    }
}
