package programmers.level02.expressionOfNum;

public class ExpressionOfNum_carnival77 {
    public int solution(int n) {
        int answer = 0;

        for(int i=1;i<n+1;i++){
            int sum=0;
            for(int j=i;j<n+1;j++){
                sum+=j;
                if(sum > n) break;
                else if(sum == n) {
                    answer+=1;
                    break;
                }
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        ExpressionOfNum_carnival77 sol = new ExpressionOfNum_carnival77();

        System.out.println(sol.solution(15));
    }
}
