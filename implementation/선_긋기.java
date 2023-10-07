package implementation;

import java.util.*;
import java.io.*;

public class 선_긋기 {

    static int N;
    static List<Point> points;

    public static void main(String[] args) throws IOException {

        inputData();

        Collections.sort(points, Comparator.comparingInt((Point p) -> p.x));

        long max = points.get(0).y;
        long len = max - points.get(0).x;
        for (int i=1; i<N; i++) {

            if (max < points.get(i).y) {
                if (max < points.get(i).x)
                    max = points.get(i).x;
                len += points.get(i).y - max;
                max = points.get(i).y;
            }
        }

        System.out.println(len);
    }

    private static void inputData() throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());
        points = new ArrayList<>();
        for (int i=0; i<N; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            int x = Integer.valueOf(st.nextToken());
            int y = Integer.valueOf(st.nextToken());
            points.add(new Point(x, y));
        }
    }

    static class Point{

        int x;
        int y;

        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}