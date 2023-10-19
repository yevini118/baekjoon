package two_pointer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 겹치는_건_싫어 {

    static int N, K;
    static int[] a;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        a = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int[] count = new int[100001];
        int max = 0;
        int start = 0;
        int end = 0;

        while(end < N) {

            while(end < N && count[a[end]] + 1 <= K) {
                count[a[end]] ++;
                end ++;
            }
            max = Math.max(max, end-start);
            count[a[start]]--;
            start++;
        }
        System.out.println(max);
    }
}