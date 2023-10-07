package implementation;

import java.io.*;
import java.util.*;

public class 달력 {

    static int N;
    static int[][] schedules;
    static int lastDay = 1;

    public static void main(String[] args) throws IOException {

        inputData();

        int[] calendar = new int[lastDay+2];
        for (int[] schedule : schedules) {
            for (int i=schedule[0]; i<=schedule[1]; i++) {
                calendar[i]++;
            }
        }

        int area = 0;
        int row = 0;
        int col = 0;
        for (int i=1; i<=lastDay+1; i++) {
            if (calendar[i] != 0) {
                col = Math.max(col, calendar[i]);
                row++;
            }
            else {
                area += col * row;
                col = 0;
                row = 0;
            }
        }

        System.out.println(area);
    }

    private static void inputData() throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        schedules = new int[N][2];
        for(int i=0; i<N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            schedules[i][0] = Integer.parseInt(st.nextToken());
            schedules[i][1] = Integer.parseInt(st.nextToken());
            lastDay = Math.max(lastDay, schedules[i][1]);
        }
    }
}
