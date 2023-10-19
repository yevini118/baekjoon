package dijkstra;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 파티 {

    static int N;
    static int M;
    static int X;
    static List<List<Node>> graph = new ArrayList<>();
    static List<List<Node>> reversedGraph = new ArrayList<>();

    static class Node implements Comparable<Node> {

        int node;
        int cost;

        public Node(int node, int cost) {
            this.node = node;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node node) {
            return this.cost - node.cost;
        }
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());

        for (int i=0; i<N+1; i++) {
            graph.add(new ArrayList<>());
            reversedGraph.add(new ArrayList<>());
        }

        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph.get(a).add(new Node(b, c));
            reversedGraph.get(b).add(new Node(a, c));
        }

        int[] go = dijkstra(reversedGraph,X);
        int[] back = dijkstra(graph, X);

        int[] minCosts = new int[N+1];
        for (int i=1; i<N+1; i++) {
            minCosts[i] = go[i] + back[i];
        }

        System.out.println(Arrays.stream(minCosts).max().getAsInt());
    }

    private static int[] dijkstra(List<List<Node>> graph, int node) {

        int INF = Integer.MAX_VALUE;
        int[] costs = new int[N+1];
        Arrays.fill(costs, INF);

        costs[node] = 0;
        PriorityQueue<Node> Q = new PriorityQueue<>();
        Q.add(new Node(node, 0));

        while (!Q.isEmpty()) {

            Node to = Q.poll();

            int p = to.cost;
            int n = to.node;

            if (costs[n] < p)
                continue;

            for (Node nod : graph.get(n)) {

                int newP = p + nod.cost;
                if (newP < costs[nod.node]) {
                    costs[nod.node] = newP;
                    Q.offer(new Node(nod.node, newP));
                }
            }
        }
        return costs;
    }
}
