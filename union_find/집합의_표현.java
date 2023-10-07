package union_find;

import java.io.*;
import java.util.*;

public class 집합의_표현 {

    static int n;
    static int m;
    static int[] parent;

    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        parent = new int[n+1];

        makeSet();

        for (int i=0; i<m; i++) {
            st = new StringTokenizer(bf.readLine());
            int c = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if (c == 0) {
                union(a, b);
            }
            else {
                isUnion(a, b);
            }
        }
    }

    private static void makeSet() {

        for(int i=0; i<n+1; i++){
            parent[i] = i;
        }
    }

    private static void union(int a, int b) {

        parent[find(b)] = find(a);
    }

    private static int find(int a) {

        if (a == parent[a])
            return a;
        return parent[a] = find(parent[a]);
    }

    private static void isUnion(int a, int b) {

        if (find(a) == find(b))
            System.out.println("YES");
        else
            System.out.println("NO");
    }
}
