package com.ktds.step01.sumOfSections.SumOfSection4_11659;

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

        int[] a = new int[N+1];
        int[] sum = new int[N+1]; // 1000의 값이 최대 100000개 --> 100000000(1억) int형으로 가능

        st = new StringTokenizer(br.readLine()," ");
        for (int i = 1; i < N+1; i++) {
            a[i]=Integer.parseInt(st.nextToken());
            sum[i]=sum[i-1]+a[i];
        }

        StringBuilder sb=new StringBuilder();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine()," ");
            int from=Integer.parseInt(st.nextToken());
            int to=Integer.parseInt(st.nextToken());
            sb.append(sum[to]-sum[from-1]).append("\n");
        }
        System.out.println(sb.toString());
    }
}
