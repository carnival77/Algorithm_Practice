package programmers.level02.KakaoFriendsColoringBook;

import java.util.*;

public class KakaoFriendsColoringBook_carnival77 {

    class Solution {
        public final int[] dx = {-1, 1, 0, 0};
        public final int[] dy = {0, 0, 1, -1};

        public void dfs(int[][] picture, int m, int n, int x, int y, int number, int cnt, int[][] group) {
            group[x][y] = cnt;

            for (int k = 0; k < 4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];
                if (0 <= nx && nx < m && 0 <= ny && ny < n) {
                    // 0이 아니고 같은 숫자이며 group이 0이라면
                    if (picture[nx][ny] == number && group[nx][ny] == 0) {
                        dfs(picture, m, n, nx, ny, number, cnt, group);
                    }
                }
            }
        }

        public int[] solution(int m, int n, int[][] picture) {
            int numberOfArea = 0;
            int maxSizeOfOneArea = 0;
            int cnt = 1;
            int[][] group = new int[m][n];
            int number = 0;

            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (picture[i][j] != 0 && group[i][j] == 0) {
                        number = picture[i][j];
                        dfs(picture, m, n, i, j, number, cnt, group);
                        cnt += 1;
                    }
                }
            }

            int[] areas = new int[cnt - 1];
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (group[i][j] != 0) {
                        areas[group[i][j] - 1] += 1;
                    }
                }
            }

            numberOfArea = cnt - 1;
            Arrays.sort(areas);
            maxSizeOfOneArea = areas[areas.length - 1];

            int[] answer = new int[2];
            answer[0] = numberOfArea;
            answer[1] = maxSizeOfOneArea;

            return answer;
        }
    }
}