package com.ktds.step02.sort.Treasure_1026;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int N=Integer.parseInt(st.nextToken());

        int[] a = new int[N];
        int[] b = new int[N];

        st = new StringTokenizer(br.readLine()," ");
        for (int i = 0; i < N; i++) {
            a[i]=Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine()," ");
        for (int i = 0; i < N; i++) {
            b[i]=Integer.parseInt(st.nextToken());
        }

        Arrays.sort(a);
        Arrays.sort(b);

        int ans=0;
        for (int i = 0; i < N; i++) {
            ans+=a[i]*b[N-i-1];
        }
        System.out.println(ans);
    }
}