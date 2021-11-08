package programmers.level01.dartGame;

import java.util.*;

public class DartGame_carnival77 {
    public int solution(String dartResult) {
        String temp = dartResult.replace("10","k");

        String[] arr = new String[temp.length()];

        for(int i=0;i<temp.length();i++){
            if(temp.charAt(i) != 'k'){
                arr[i]=String.valueOf(temp.charAt(i));
            }
            else{
                arr[i]="10";
            }
        }

        int s_inx=-1;
        int[] stages = new int[3];

        for(String ele : arr){
            if(ele.equals("D")){
                stages[s_inx] = (int) Math.pow(stages[s_inx],2);continue;
            }
            else if(ele.equals("T")){
                stages[s_inx] = (int) Math.pow(stages[s_inx],3); continue;
            }
            else if(ele.equals("S")) continue;
            else if(ele.equals("#")){
                stages[s_inx] = -stages[s_inx]; continue;
            }
            else if(ele.equals("*")){
                stages[s_inx] *= 2;
                if(s_inx > 0){
                    stages[s_inx-1] *= 2;
                }
                continue;
            }
            else{
                s_inx+=1;
                stages[s_inx] = Integer.parseInt(ele);
            }
        }

        return Arrays.stream(stages).sum();
    }

    public static void main(String[] args) {
        String dartResult = "1S2D*3T";

        DartGame_carnival77 sol = new DartGame_carnival77();

        System.out.println(sol.solution(dartResult));
    }
}
