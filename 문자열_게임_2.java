import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 문자열_게임_2 {

    static int K;
    static char[] w;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i=0; i<T; i++) {
            String W = br.readLine();
            K = Integer.parseInt(br.readLine());
            w = W.toCharArray();
            solution();
        }
    }
    
    private static void solution() {

        int answer3 = Integer.MAX_VALUE;
        int answer4 = 0;
        for (int i=0; i<w.length-K; i++) {
            int c = 0;
            for (int j=i; j<w.length; j++) {
                if (w[i] == w[j])
                    c ++;
                if (c==K) {
                    answer3 = Math.min(answer3, j-i+1);
                    answer4 = Math.max(answer4, j-i+1);
                    break;
                }
            }
        }

        if (answer4 == 0)
            System.out.println(-1);
        else
            System.out.println(answer3 + " " + answer4);
    }
}
