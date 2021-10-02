package programmers.level02.NormalSquare;

public class NormalSquare_carnival77 {
    // 멀쩡한 사각형
    public long solution(int w, int h) {
        long answer = 0;



        long gcd = GCD(w,h);
        answer = (long)w*(long)h - gcd*((long)w/gcd+(long)h/gcd-1);


        return answer;
    }

    static int GCD(int a, int b){ // 최대공약수
        if (a%b == 0) {
            return b;
        }
        return GCD(b, a % b);
    }

    public static void main(String[] args) {


        int W = 8;
        int H = 12;
        NormalSquare_carnival77 sol = new NormalSquare_carnival77();
        sol.solution(W, H);

    }
}
