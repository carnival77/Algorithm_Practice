package programmers.level02.joystick;

public class joystick_carnival77 {
    public int solution(String name) {
        int answer = 0;
        int len = name.length();

        // 처음부터 끝까지 오른쪽으로 갈 때의 이동횟수
        // 제일 짧은 좌, 우 이동은 그냥 맨 오른쪽으로 이동할 때
        int min = len - 1;

        for (int i = 0; i < len; i++) {
            // 조이스틱 상, 하 이동
            char c = name.charAt(i);
            int mov = (c - 'A' < 'Z' - c + 1) ? (c - 'A') : ('Z' - c + 1);
            answer += mov;

            // 조이스틱 좌, 우 이동
            int nextIndex = i + 1;
            // 다음 단어가 A이고, 단어가 끝나기 전까지 nextIndex 증가
            while (nextIndex < len && name.charAt(nextIndex) == 'A')
                nextIndex++;

            min = Math.min(min, (i * 2) + len - nextIndex);
//            그리고 BBBAAAAAABA 이런식으로 중간까지 왔다 다시 왼쪽으로 돌아가는 것이 더 빠른 경우가 있다.
//            이 코드가 min = Math.min(min, (i * 2) + len - nextIndex); 다.
//            ì * 2 는 중간까지 왔다가 다시 뒤로 돌아갈 때의 조이스틱 이동 횟수이고,
//            len - nextIndex 는 예시의 오른쪽에서 두번째의 B같은 애들까지의 위치
        }

        answer += min;

        return answer;
    }

    public static void main(String[] args) {

        String name = "JAN";

        joystick_carnival77 sol = new joystick_carnival77();
        sol.solution(name);

    }

}
