// level3 [1차]추석 트래픽

package programmers.level03;

import java.text.SimpleDateFormat;
import java.util.*;

public class thanksGivingTraffic_carnival77 {
    public static int solution(String[] lines) throws Exception {
        SimpleDateFormat format = new SimpleDateFormat("HH:mm:ss.SSS");

        int[] counts = new int[lines.length];
        int max = 0;

        for(int i=0; i<lines.length; i++) {
            // 이전 로그의 완료 시점
            String[] pre = lines[i].split(" ");
            Date preEndDate = format.parse(pre[1]);
            long preEnd = preEndDate.getTime();

            // 해당 로그의 다음 로그들 중 해당 로그가 끝나기 전에 시작하는 로그 체크
            for (int j = i ; j < lines.length; j++) {
                // 다음 로그의 시작시점
                String[] next = lines[j].split(" ");
                Date nextEndDate = format.parse(next[1]);
                double sec = Double.parseDouble(next[2].substring(0, next[2].length()-1)); // 처리 시간

                // 다음 로그의 시작 시점 = 다음 로그의 종료 시점 - 처리 초 + 1;
                // ex) 문제에서 보면 알듯 2016-09-15 01:00:07.000 2s는
                // 01:00:05.001 ~ 01:00:07.000에서 2초 동안 처리된다.
                // 7,000 - 2,000 + 1 = 5.001
                long nextStart = (long) (nextEndDate.getTime() - sec*1000 + 1);

                // 이전 로그의 종료시점부터 + 1초 범위안에 시작되면 + 1
                // 1부터 10의 범위를 가진다고 하면
                // 1 2 3 4 5 6 7 8 9 10 이렇게 가진다.
                // 1 + 10 = 11 이므로 = 부호를 사용하면 안됨
                if(preEnd + 1000 > nextStart) {
                    counts[i] += 1;
                    max = Math.max(max, counts[i]);
                }
            }
        }
        return max;
    }
}
