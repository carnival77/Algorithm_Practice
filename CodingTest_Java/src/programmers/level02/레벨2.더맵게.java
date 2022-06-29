package com.ktds.step03.dataStructure;

import java.util.PriorityQueue;

public class 더맵게 {
    static class Solution {
        public int solution(int[] scoville, int K) {
            PriorityQueue<Integer> q=new PriorityQueue<>();
            int ans=0;

            for (int s:scoville
            ) {
                q.offer(s);
            }

            while(true){
                if(q.peek()>=K){
                    return ans;
                }
                if(q.size()<2){
                    return -1;
                }
                int first=q.poll();
                int second=q.poll();
                q.offer(first+second*2);
                ans+=1;
            }
        }
    }

    public static void main(String[] args) {
        Solution s=new Solution();
        int[] scoville=new int[]{1, 2, 3, 9, 10, 12};
        int K=7;
        System.out.println(s.solution(scoville,K));
    }
}
