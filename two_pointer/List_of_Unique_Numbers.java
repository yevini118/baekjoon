package two_pointer;

import java.awt.print.Pageable;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;

public class List_of_Unique_Numbers {

    static int N;
    static int[] nums;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        nums = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int[] count = new int[100001];
        long answer = 0;
        int end = -1;
        for (int start=0; start<N; start++) {
            while(end+1 < N && count[nums[end+1]] == 0) {
                end++;
                count[nums[end]]++;
            }
            answer += end - start + 1;
            count[nums[start]]--;
        }
        System.out.println(answer);
    }
}
