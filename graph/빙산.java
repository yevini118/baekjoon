import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;


public class 빙산 {

    static int N;
    static int M;
    static int[][] sea;

    static int[] dn = {0, 0, 1, -1};
    static int[] dm = {1, -1, 0, 0};

    public static void main(String[] args) throws Exception {

        //input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        sea = new int[N][M];

        for(int n=0; n<N; n++) {
            st = new StringTokenizer(br.readLine());
            for(int m=0; m<M; m++) {
                sea[n][m] = Integer.parseInt(st.nextToken());
            }
        }


        int year = 0;
        while(true) {

            boolean[][] visit = new boolean[N][M];
            int area = 0;

            for(int n=0; n<N; n++) {
                for(int m=0; m<M; m++) {
                    if (sea[n][m] != 0 && !visit[n][m]) {
                        bfs(visit, new Point(n, m));
                        area += 1;
                    }
                }
            }

            if (area >= 2) {
                System.out.println(year);
                break;
            }
            if (area == 0) {
                System.out.println(0);
                break;
            }
            year += 1;
        }
    }

    private static void bfs(boolean[][] visit, Point point) {

        Queue<Point> queue = new LinkedList<>();
        queue.offer(point);
        visit[point.n][point.m] = true;

        while(!queue.isEmpty()) {

            Point p = queue.poll();

            for(int i=0; i<4; i++) {
                int nn = p.n + dn[i];
                int nm = p.m + dm[i];

                if (!visit[nn][nm]) {
                    if (sea[nn][nm] == 0 && sea[p.n][p.m] > 0) {
                        sea[p.n][p.m] -= 1;
                    }
                    if (sea[nn][nm] != 0) {
                        queue.offer(new Point(nn, nm));
                        visit[nn][nm] = true;
                    }
                }
            }
        }
    }

    public static class Point{
        int n;
        int m;

        Point(int n, int m) {
            this.n = n;
            this.m = m;
        }
    }
}