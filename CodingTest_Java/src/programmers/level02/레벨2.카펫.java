package programmers.level02.carpet;

public class Carpet_carnival77 {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];

        int t = brown + yellow;

        for(int x=t;x>0;x--){
            if(t%x == 0){
                int y=t/x;
                if((x-2)*(y-2) == yellow){
                    answer[0]=y;
                    answer[1]=x;
                }
            }
        }

        return answer;
    }
}
