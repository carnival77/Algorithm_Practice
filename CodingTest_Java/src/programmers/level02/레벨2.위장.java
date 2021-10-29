package programmers.level02.camouflage;
import java.util.*;
public class Camouflage_carnival77 {

    public Map<String,Integer> counter1(List<String> list){
        Map<String, Integer> counter = new HashMap<String, Integer>();

        for (String ele : list) {
            Integer previousValue = counter.get(ele);

            counter.put(ele, previousValue == null ? 1 : previousValue+1 );
        }

        return counter;
    }

    public int solution(String[][] clothes) {
        int answer = 1;

        ArrayList<String> kinds = new ArrayList<>();

        int n=clothes.length;

        for(int i=0;i<n;i++){
            kinds.add(clothes[i][1]);
        }

        Map<String,Integer> counter = counter1(kinds);

        for(String s : counter.keySet()){
//            System.out.println(counter.get(s));
            answer *= counter.get(s);
        }

        return answer-1;
    }


    public int solution2(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> map = new HashMap<>();
        for(int i=0; i<clothes.length; i++){
            String key = clothes[i][1];
            if(!map.containsKey(key)) {
                map.put(key, 1);
            } else {
                map.put(key, map.get(key) + 1);
            }
        }
        Iterator<Integer> it = map.values().iterator();
        while(it.hasNext()) {
            answer *= it.next().intValue()+1;
        }
        return answer-1;
    }
}
