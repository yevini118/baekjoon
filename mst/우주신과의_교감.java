import java.util.*;
import java.io.*;

public class 우주신과의_교감 {

    static int N;
    static int M;

    static int[] parent;
    static Point[] points;
    static List<Edge> edges = new ArrayList<>();

    static class Point {
        int x;
        int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static class Edge {

        int a;
        int b;
        double distance;

        public Edge(int a, int b, double distance) {
            this.a = a;
            this.b = b;
            this.distance = distance;
        }
    }
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        points = new Point[N+1];
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            points[i+1] = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }

        parent = new int[N+1];
        makeSet();
        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            union(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }

        makeEdges();
        edges.sort(Comparator.comparing(e -> e.distance));

        double cost = 0;
        for(Edge edge : edges) {
            if(!isCycle(edge.a, edge.b)) {
                union(edge.a, edge.b);
                cost += edge.distance;
            }
        }

        System.out.println(String.format("%.2f", cost));
    }

    private static void makeEdges() {
        for (int i=1; i<=N; i++) {
            for (int j=i+1; j<=N; j++) {
                edges.add(new Edge(i, j, calculateDistance(points[i], points[j])));
            }
        }
    }

    private static void makeSet() {

        for (int i=1; i<=N; i++) {
            parent[i] = i;
        }
    }

    private static int find(int a) {

        if (a == parent[a])
            return a;
        return parent[a] = find(parent[a]);
    }

    private static void union(int a, int b) {

        parent[find(b)] = find(a);
    }

    private static boolean isCycle(int a, int b) {

        return find(a) == find(b);
    }

    private static double calculateDistance(Point a, Point b) {
        return Math.sqrt(Math.pow(a.x - b.x,2) + Math.pow(a.y - b.y, 2));
    }
}