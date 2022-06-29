package com.ktds.step03.dataStructure;

import java.util.Collections;
import java.util.PriorityQueue;

public class 프린터 {
    static class Solution {
        public int solution(int[] priorities, int location) {
            PriorityQueue<Integer> q = new PriorityQueue<>(Collections.reverseOrder());
            // 우선순위 큐를 활용해, 중요도가 높은 순으로 큐를 정렬한다.
            int ans=1;
            // location과 ans는 priorities에서 몇 번째 우선순위를 가진 요소가
            // 몇 번째에 출력되는 지를 나타낸다.
            for (int p:priorities
            ) {
                q.offer(p);
            }

            while(!q.isEmpty()){ // 큐가 빌 때까지, 우선순위가 높은 순으로 큐에서 제거한다.
                for (int i = 0; i < priorities.length; i++) {
                    if(q.peek() == priorities[i]){
                        // 가장 높은 우선순위를 가진 요소를 priorities에서 발견하고
                        if(location==i){
                            // 타겟 우선순위를 가리키는 location과 일치하면,
                            return ans;
                            // 몇 번째에 출력되는 지 ans를 반환한다.
                        }
                        q.poll(); // 가장 높은 우선순위를 가진 요소를 큐에서 제거한다(출력한다)
                        ans+=1; // 출력 순서를 1 증가시킨다.
                    }
                }
            }
            return ans;
        }
    }

    public static void main(String[] args) {
        Solution s=new Solution();
        int[] priorities=new int[]{2, 1, 3, 2};
        int location=0;
        System.out.println(s.solution(priorities,location));
    }

}
