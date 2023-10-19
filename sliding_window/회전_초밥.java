package sliding_window;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 회전_초밥 {

    static int N, d, k, c;
    static int[] sushi;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        sushi = new int[N];

        for (int i=0; i<N; i++) {
            sushi[i] = Integer.parseInt(br.readLine());
        }

        int[] visit = new int[d+1];
        int max = 0;
        for (int i=0; i<k; i++) {
            if (visit[sushi[i]] == 0)
                max ++;
            visit[sushi[i]] ++;
        }

        int count = max;
        for(int i=0; i<N; i++) {

            if (visit[c] == 0)
                max = Math.max(max, count+1);
            else
                max = Math.max(max, count);

            visit[sushi[i]] --;
            if (visit[sushi[i]] == 0)
                count--;

            int j = (i+k) % N;
            if (visit[sushi[j]] == 0)
                count++;
            visit[sushi[j]] ++;
        }
        System.out.println(max);
    }
}
