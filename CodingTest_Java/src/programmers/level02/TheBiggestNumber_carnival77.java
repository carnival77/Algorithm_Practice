package programmers.level02.theBiggestNumber;
import java.util.*;
public class TheBiggestNumber_carnival77 {
    public String solution(int[] numbers) {
        String answer = "";

        String[] str_nums = new String[numbers.length];

        for(int i=0;i<numbers.length;i++){
            str_nums[i] = Integer.toString(numbers[i]);
        }

        Arrays.sort(str_nums, new Comparator<String>(){
            @Override
            public int compare(String s1, String s2){
                return (s2+s1).compareTo(s1+s2);
            }
        });

        if(str_nums[0].equals("0")) return "0";

        for(String s : str_nums) answer += s;

        return answer;
    }
}

// 람다를 사용한 풀이

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";

        List<Integer> list = new ArrayList<>();
        for(int i = 0; i < numbers.length; i++) {
            list.add(numbers[i]);
        }
        Collections.sort(list, (a, b) -> {
            String as = String.valueOf(a), bs = String.valueOf(b);
            return -Integer.compare(Integer.parseInt(as + bs), Integer.parseInt(bs + as));
        });
        StringBuilder sb = new StringBuilder();
        for(Integer i : list) {
            sb.append(i);
        }
        answer = sb.toString();
        if(answer.charAt(0) == '0') {
            return "0";
        }else {
            return answer;
        }
    }
}