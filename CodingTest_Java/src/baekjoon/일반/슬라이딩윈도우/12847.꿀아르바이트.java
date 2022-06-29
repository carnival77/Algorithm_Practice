package com.ktds.step01.slidingWindow.HoneyPartTimeJob_12847;

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

        Long[] a = new Long[N];

        long sum=0;
        st = new StringTokenizer(br.readLine()," ");
        for (int k = 0; k < N; k++) {
            a[k]=Long.parseLong(st.nextToken());
        }

        for (int k = 0; k < M; k++) {
            sum+=a[k];
        }

        long max=sum;
        for (int s = 0; s+M<N; s++) {
            sum+=a[s+M];
            sum-=a[s];
            max=Math.max(sum,max);
        }
        System.out.println(max);
//        while(j<M-1){
//            a[j]=Integer.parseInt(st.nextToken());
//            sum+=a[j++];
//        }
//
//        int max=0;
//
//        while(j<N){
//            a[j]=Integer.parseInt(st.nextToken());
//            sum+=a[j++];
//            max=Math.max(sum,max);
//            sum-=a[i++];
//        }
//        System.out.println(max);
    }
}
