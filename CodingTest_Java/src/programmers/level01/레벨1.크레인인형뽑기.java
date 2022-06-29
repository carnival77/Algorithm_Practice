package com.ktds.step03.dataStructure;

import java.util.Stack;

public class 크레인인형뽑기 {
    static class Solution {
        public int solution(int[][] board, int[] moves) {
            Stack<Integer> st=new Stack<>();
            int n=board.length;
            int ans=0;
            for (int move:moves
            ) {
                int col=move-1;
                for(int row=0;row<n;row++){
                    if(board[row][col]!=0){
                        st.push(board[row][col]);
                        board[row][col]=0;
                        break;
                    }
                }
                if(st.size()>=2){
                    int tmp=st.pop();
                    int tmp2=st.peek();
                    if(tmp==tmp2){
                        st.pop();
                        ans+=2;
                    }
                    else{
                        st.push(tmp);
                    }
                }
            }

            return ans;
        }
    }

    public static void main(String[] args) {
        Solution s=new Solution();
        int[][] board=new int[][]{{0,0,0,0,0},{0,0,1,0,3},{0,2,5,0,1},{4,2,4,4,2},{3,5,1,3,1}};
        int[] moves=new int[]{1,5,3,5,1,2,1,4};
        System.out.println(s.solution(board,moves));
    }
}