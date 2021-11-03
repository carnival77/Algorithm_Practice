package programmers.level02.rotateBracket;

import java.util.*;

public class RotateBracket_carnival77 {
    static int answer=0;
    static int n=0;

    public boolean check(String s){
        Stack<Character> stack = new Stack<>();
        for(int i=0;i<n;i++){
            char c = s.charAt(i);
            if(c == '(' || c == '{' || c == '['){
                stack.add(c);
            }
            else{
                if(stack.empty()){
                    return false;
                }
                else{
                    char tg = stack.pop();
                    if(c==')' && tg != '(')
                        return false;
                    else if(c=='}' && tg != '{')
                        return false;
                    else if(c==']' && tg != '[')
                        return false;
                }
            }
        }
        return stack.empty();
    }

    public int solution(String s) {
        n=s.length();

        for(int x=0;x<n;x++){
            String s2 = s.substring(x,n) + s.substring(0,x);
            if (check(s2)){
                answer+=1;
            }
        }



        return answer;
    }

    public static void main(String[] args) {

        String s = "[](){}";

        RotateBracket_carnival77 stringComp = new RotateBracket_carnival77();
        System.out.println(stringComp.solution(s));

    }
}
