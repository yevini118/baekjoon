import java.io.*;
import java.util.*;

public class 수_정렬하기2 {

    static int N;
    static List<Integer> nums;

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        nums = new ArrayList<>();
        for (int i=0; i<N; i++) {
            nums.add(Integer.parseInt(br.readLine()));
        }

        Collections.sort(nums);

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for(int n: nums) {
            bw.write(n+"\n");
        }
        bw.flush();
        bw.close();
    }
}
