package unsolve;

import java.io.*;
import java.util.*;

public class 부분수열의_합 {

    static int N;
    static int S;
    static int[] nums;
    static int count;

    public static void main(String[] args) throws IOException{

        inputData();
        back(0, 0);

        if (S==0 && count > 0)
            count --;
        System.out.println(count);
    }

    private static void back(int start, int sum) {

        if (start == N) {
            if (sum == S) {
                count ++;
            }
            return;
        }

        back(start + 1 , sum);
        back(start + 1, sum + nums[start]);
    }

    private static void inputData() throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        N = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());
        nums = Arrays.stream(bf.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
    }
}