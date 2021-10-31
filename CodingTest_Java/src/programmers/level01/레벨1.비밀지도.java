package programmers.level01.secretMap;
import programmers.level01.failureRate.FailureRate_carnival77;

import java.util.*;
public class SecretMap_carnival77 {
    public String[] solution(int n, int[] arr1, int[] arr2) {

        String[] answer = new String[n];

        char[][] map = new char[n][n];

        for (int i = 0; i < n; i++) {
            String str1_ = Integer.toBinaryString(arr1[i]);
            String str2_ = Integer.toBinaryString(arr2[i]);

            String str1="";
            String str2="";

            int rest = n- str1_.length();

            for(int x=0;x<rest;x++){
                str1 += "0";
            }
            str1 += str1_;

            rest=n-str2_.length();

            for(int x=0;x<rest;x++){
                str2 += "0";
            }
            str2 += str2_;

            for (int j = 0; j < str1.length(); j++) {
                if (str1.charAt(j) == '1' || str2.charAt(j) == '1') {
                    map[i][j] = '#';
                } else if (str1.charAt(j) == '0' && str2.charAt(j) == '0') {
                    map[i][j] = ' ';
                }
            }
        }

        for(int i=0;i<n;i++) {
            char[] chars = new char[n];
            for(int j=0;j<n;j++){
                chars[j] = map[i][j];
            }
            String str = new String(chars);
            answer[i] = str;
        }

        return answer;
    }

    public String[] solution2(int n, int[] arr1, int[] arr2) {
        String[] result = new String[n];
        for (int i = 0; i < n; i++) {
            result[i] = Integer.toBinaryString(arr1[i] | arr2[i]);
        }

        for (int i = 0; i < n; i++) {
            result[i] = String.format("%" + n + "s", result[i]);
            result[i] = result[i].replaceAll("1", "#");
            result[i] = result[i].replaceAll("0", " ");
        }

        return result;
    }

    public static void main(String[] args) {

//        int n = 5;
//        int[] arr1 = {9, 20, 28, 18, 11};
//        int[] arr2 = {30, 1, 21, 17, 28};

        int n = 6;
        int[] arr1 = {46, 33, 33 ,22, 31, 50};
        int[] arr2 = {27 ,56, 19, 14, 14, 10};


        SecretMap_carnival77 sol = new SecretMap_carnival77();
        System.out.println(sol.solution2(n,arr1,arr2));

    }
}