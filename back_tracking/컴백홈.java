package back_tracking;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 컴백홈 {

    static int R, C, K;
    static char[][] ways;

    static boolean[][] visit;
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    static int count = 0;

    static class Point {
        int x;
        int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        ways = new char[R][];
        for (int i=0; i<R; i++) {
            ways[i] = br.readLine().toCharArray();
        }

        visit = new boolean[R][C];
        visit[R-1][0] = true;
        back(new Point(0, R-1), 1);
        System.out.println(count);
    }

    private static void back(Point p, int depth) {

        if (p.x == C-1 && p.y == 0) {
            System.out.println(depth);
            if (depth == K)
                count ++;
            return;
        }

        for (int i=0; i<4; i++) {
            int nx = p.x + dx[i];
            int ny = p.y + dy[i];

            if (0<= nx && nx < C && 0<= ny && ny < R) {
                if (ways[ny][nx] != 'T' && !visit[ny][nx]) {
                    visit[ny][nx] = true;
                    back(new Point(nx, ny), depth+1);
                    visit[ny][nx] = false;
                }
            }
        }
    }
}
