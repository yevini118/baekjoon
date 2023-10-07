package union_find;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 사이클_게임 {

    static int n;
    static int m;
    static int[] parent;

    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        parent = new int[n];

        makeSet();
        for (int i=0; i<m; i++) {
            st = new StringTokenizer(bf.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if (isCycle(a, b)) {
                System.out.println(i+1);
                return;
            }
            union(a, b);
        }
        System.out.println("0");
    }

    private static void makeSet() {

        for (int i=0; i<n; i++) {
            parent[i] = i;
        }
    }

    private static int find(int a) {

        if(a == parent[a])
            return a;
        return parent[a] = find(parent[a]);
    }

    private static void union(int a, int b) {

        parent[find(b)] = find(a);
    }

    private static boolean isCycle(int a, int b) {

        return find(a) == find(b);
    }
}
