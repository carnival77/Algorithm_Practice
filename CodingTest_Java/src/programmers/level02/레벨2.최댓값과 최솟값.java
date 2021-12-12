package programmers.level02.maxAndMin;

import java.util.*;

public class MaxAndMin_carnival77 {
    public String solution(String s) {
        String answer = "";

        ArrayList<Integer> nums = new ArrayList<>();
        String[] str_nums = s.split(" ");

        for(int i=0; i<str_nums.length; i++) {
            nums.add(Integer.parseInt(str_nums[i]));
        }

        answer = Collections.min(nums).toString() + ' ' + Collections.max(nums).toString();

        return answer;
    }

    public static void main(String[] args) {
        MaxAndMin_carnival77 sol = new MaxAndMin_carnival77();

        String s = "-1 -2 -3 -4";

        System.out.println(sol.solution(s));
    }
}
