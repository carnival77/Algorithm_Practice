package programmers.level02.makeBigNum;

import java.util.*;
import java.util.stream.Stream;

public class MakeBigNum_carnival77 {
    public String solution(String number, int k) {
        String answer = "";

        Stack<Integer> stack = new Stack<>();

        int[] numbers = Stream.of(number.split("")).mapToInt(Integer::parseInt).toArray();

        int n=number.length();

        for(int i=0;i<n;i++){
            while(k>0 && !stack.empty() && stack.peek() < numbers[i]){
                stack.pop();
                k-=1;
            }
            stack.push(numbers[i]);
        }

        for(int i : stack){
            answer+=String.valueOf(i);
        }

        answer=answer.substring(0,answer.length()-k);

        return answer;
    }
}
