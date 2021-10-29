package programmers.level02.lightCycle;

import java.util.*;
public class LightCycle_carnival77 {
//    class Solution {

    static int R, C;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, -1, 0, 1};
    static boolean[][][] visit;

    public int[] solution(String[] grid) {
        ArrayList<Integer> answer = new ArrayList<Integer>();

        R = grid.length;
        C = grid[0].length();

        visit = new boolean[R][C][4];

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                for (int d = 0; d < 4; d++) {
                    if(visit[i][j][d] == false) {
                        answer.add(lightCycle(grid, i, j, d));
                    }
                }
            }
        }

        return answer.stream().sorted().mapToInt(i -> i).toArray();
    }

    public int lightCycle(String[] grid, int r, int c, int d) {
        int cnt = 0;

        while (true) {
            if (visit[r][c][d] == true) {
                break;
            }



            visit[r][c][d] = true;
            cnt = cnt + 1;

            if (grid[r].charAt(c) == 'L') {
                d = (d + 3) % 4;
            } else if (grid[r].charAt(c) == 'R') {
                d = (d + 1) % 4;
            }

            r = (r + dr[d] + R) % R;
            c = (c + dc[d] + C) % C;

        }
        return cnt;
    }

    //    }
    public static void main(String[] args) {

        String[] grid = {"SL","LR"};

        LightCycle_carnival77 sol = new LightCycle_carnival77();
        System.out.println(sol.solution(grid));
    }
}
