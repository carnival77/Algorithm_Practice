package com.ktds.step01.sumOfSections.SumOfSection5_11660;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int N=Integer.parseInt(st.nextToken());
        int M=Integer.parseInt(st.nextToken());

        int[][] a = new int[N+1][N+1];
        int[][] sum = new int[N+1][N+1]; // 1000의 값이 최대 100000개 --> 100000000(1억) int형으로 가능

        for (int i = 1; i < N+1; i++) {
            st = new StringTokenizer(br.readLine()," ");
            for (int j=1;j<N+1;++j){
                a[i][j]=Integer.parseInt(st.nextToken());
                sum[i][j]=sum[i][j-1]+sum[i-1][j]-sum[i-1][j-1]+a[i][j];
            }
        }

        StringBuilder sb=new StringBuilder();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine()," ");
            int x1=Integer.parseInt(st.nextToken());
            int y1=Integer.parseInt(st.nextToken());
            int x2=Integer.parseInt(st.nextToken());
            int y2=Integer.parseInt(st.nextToken());
            sb.append(sum[x2][y2]-sum[x1-1][y2]-sum[x2][y1-1]+sum[x1-1][y1-1]).append("\n");
        }
        System.out.println(sb.toString());
    }
}
