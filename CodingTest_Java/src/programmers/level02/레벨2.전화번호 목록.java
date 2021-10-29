package programmers.level02.phoneNumList;
import programmers.level02.lightCycle.LightCycle_carnival77;

import java.util.*;

public class PhoneNumList_carnival77 {
    public boolean solution1(String[] phone_book) {
        boolean answer = true;
        Map<String,Integer> map = new HashMap();
        for(int i=0;i<phone_book.length;i++){
            map.put(phone_book[i],i);
        }
        for(int i=0;i<phone_book.length;i++){
            String phone_number = phone_book[i];
            String temp="";
            for(int j=0;j<phone_number.length();j++){
                char number = phone_number.charAt(j);
                temp = temp + number;
                if(map.containsKey(temp) && !temp.equals(phone_number)){
                    answer=false;
                    return answer;
                }
            }
        }

        return answer;
    }

    // substring 사용
    public boolean solution2(String[] phoneBook) {
        boolean answer = true;

        Map<String, Integer> map = new HashMap<>();

        for(int i = 0; i < phoneBook.length; i++) {
            map.put(phoneBook[i], i);
        }


        for(int i = 0; i < phoneBook.length; i++) {
            for(int j = 0; j < phoneBook[i].length(); j++) {
                if(map.containsKey(phoneBook[i].substring(0,j))) {
//                    System.out.println(phoneBook[i].substring(0,j));
                    answer = false;
                    return answer;
                }
            }
        }
        return answer;
    }

    public static void main(String[] args) {

        String[] phone_book = {"119", "97674223", "1195524421"};

        PhoneNumList_carnival77 sol = new PhoneNumList_carnival77();
        System.out.println(sol.solution2(phone_book));
    }
}
