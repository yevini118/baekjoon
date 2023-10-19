import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 두_용액 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] liquid = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        Arrays.sort(liquid);

        int start = 0;
        int end = N-1;
        int[] answer = new int[2];
        int sum = Integer.MAX_VALUE;

        while(start < end) {

            int result = liquid[start] + liquid[end];
            if (sum > Math.abs(result)) {
                sum = Math.abs(result);
                answer[0] = liquid[start];
                answer[1] = liquid[end];
            }

            if(result < 0)
                start ++;
            else
                end --;
        }
        System.out.println(answer[0] + " " + answer[1]);
    }
}
