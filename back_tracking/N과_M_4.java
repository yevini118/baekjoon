package back_tracking;

import java.util.*;
import java.io.*;

public class N과_M_4 {

    static int N;
    static int M;
    static int[] nums;

    public static void main(String[] args) throws IOException {

        inputData();

        back(1, 0);
    }

    private static void back(int start, int depth){

        if (depth == M) {
            print();
            return;
        }

        for (int i=start; i<=N; i++) {
            nums[depth] = i;
            back(i, depth+1);
        }

    }

    private static void print() {
        StringBuilder print = new StringBuilder();
        for (int i=0; i<M; i++) {
            print.append(nums[i]).append(" ");
        }
        System.out.println(print.toString());
    }

    private static void inputData() throws IOException{

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        nums = new int[M];
    }
}
