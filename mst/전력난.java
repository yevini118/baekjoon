package mst;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class 전력난 {

    static class Edge {

        int x;
        int y;
        int z;

        Edge(int x, int y, int z) {
            this.x = x;
            this.y = y;
            this.z = z;
        }
    }

    static int m;
    static int n;
    static List<Edge> edges;
    static int[] parent;
    static int total;

    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        while(true) {

            inputData(bf);
            if (m==0 && n==0)
                break;

            makeSet();
            edges.sort(Comparator.comparing(e -> e.z));

            int count = 0;
            int cost = 0;
            for (Edge edge : edges) {

                if(!isCycle(edge.x, edge.y)) {
                    cost += edge.z;
                    union(edge.x, edge.y);
                    count ++;
                }

                if(count == m-1)
                    break;
            }
            System.out.println(total - cost);
        }
    }

    private static void makeSet() {

        for(int i=0; i<m; i++) {
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

    private static void inputData(BufferedReader bf) throws IOException {
        StringTokenizer st = new StringTokenizer(bf.readLine());

        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        parent = new int[m];
        total = 0;

        edges = new ArrayList<>();
        for (int i=0; i<n; i++) {
            st = new StringTokenizer(bf.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int z = Integer.parseInt(st.nextToken());
            total += z;
            edges.add(new Edge(x, y, z));
        }
    }
}
