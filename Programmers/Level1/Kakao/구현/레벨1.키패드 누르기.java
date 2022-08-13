import java.util.*;

class Point{
    int x;
    int y;
    Point(int x,int y){
        this.x = x;
        this.y = y;
    }
}

class Solution {
public String solution(int[] numbers, String hand) {
        String answer = "";

        Point left = new Point(3, 0);
        Point right = new Point(3, 2);

        for (int n : numbers) {
            int x = n / 3;
            if (n == 1 || n == 4 || n == 7) {
                left = new Point(x, 0);
                answer += "L";
            } else if (n == 3 || n == 6 || n == 9) {
                right = new Point(x - 1, 2);
                answer += "R";
            } else {
                if (n == 0) x = 3;
                int left_dist = Math.abs(left.x - x) + Math.abs(left.y - 1);
                int right_dist = Math.abs(right.x - x) + Math.abs(right.y - 1);
                if (left_dist > right_dist) {
                    right = new Point(x, 1);
                    answer += "R";
                } else if (left_dist < right_dist) {
                    left = new Point(x, 1);
                    answer += "L";
                } else {
                    if (hand.equals("left")) {
                        left = new Point(x, 1);
                        answer += "L";
                    } else {
                        right = new Point(x, 1);
                        answer += "R";
                    }
                }
            }
        }

        return answer;
    }
}