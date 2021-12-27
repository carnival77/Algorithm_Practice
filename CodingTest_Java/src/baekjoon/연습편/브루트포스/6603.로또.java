package baekjoon.practice.bruteForce.lotto_6603;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Lotto_6603_carnival77 {

//    public class Main {

        static StringBuilder sb;
        static int[] numbers;
        static boolean[] isUsed;
        static int[] result;
        static int k;

        public static void main(String[] args) throws IOException{

            sb = new StringBuilder();
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st;

            while(true) {
                st = new StringTokenizer(br.readLine());
                k = Integer.parseInt(st.nextToken());

                if(k == 0) break;

                numbers = new int[k];
                isUsed = new boolean[k];
                result = new int[6];

                for (int i = 0; i < k; i++) {
                    numbers[i] = Integer.parseInt(st.nextToken());
                }

                dfs(0,0);
                sb.append("\n");
            }

            System.out.println(sb.toString());

        }

        private static void dfs(int index,int start) {
            if(index == 6) {
                for (int i = 0; i < 6; i++) {
                    sb.append(result[i]);
                    sb.append(" ");
                }
                sb.append("\n");
                return;
            }

            for (int i = start; i < k; i++) {

                if(isUsed[i]) continue;
                isUsed[i] = true;
                result[index] = numbers[i];
                dfs(index+1,i+1);
                isUsed[i] = false;

            }
        }
//    }
}