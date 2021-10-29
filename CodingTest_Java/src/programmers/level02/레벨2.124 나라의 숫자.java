package programmers.level02.countryOf124;

public class ContryOf124_carnival77 {
    public String solution(int n) {

       String[] numbers={"4","1","2"};
       String answer="";

       while (n>0) {
           int remain = n % 3;
           n /= 3;

           if (remain == 0) n -= 1;

           answer = numbers[remain] + answer;
       }
        return answer;
    }

    public static void main(String[] args) {


        int n = 4;
        ContryOf124_carnival77 sol = new ContryOf124_carnival77();
        sol.solution(n);

    }
}
