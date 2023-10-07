package back_tracking;

import java.util.*;
import java.io.*;

public class 외판원_순회_2 {

    static int N;
    static int[][] cost;
    static int min = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException{

        inputData();

        for (int i=0; i<N; i++) {
            if (cost[0][i] != 0) {
                boolean[] visited = new boolean[N];
                visited[0] = true;
                visited[i] = true;
                back(visited, 0, i, 1, cost[0][i]);
            }
        }
        System.out.println(min);
    }

    private static void back(boolean[] visited, int start, int end, int depth, int sum) {

        if(depth == N-1) {
            if (cost[end][start] != 0) {
                min = Math.min(min, sum + cost[end][start]);
            }
            return;
        }
        for(int i=0; i<N; i++) {
            if (!visited[i] && cost[end][i] != 0) {
                visited[i] = true;
                back(visited, start, i, depth + 1, sum + cost[end][i]);
                visited[i] = false;
            }
        }
    }

    private static void inputData() throws IOException{

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(bf.readLine());
        cost = new int[N][];
        for (int i=0; i<N; i++) {
            cost[i] = Arrays.stream(bf.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }
    }
}
