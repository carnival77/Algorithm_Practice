package programmers.level01.failureRate;

import java.util.*;
import java.util.Map.Entry;

public class FailureRate_carnival77 {

    // 나의 풀이 : HashMap, ArrayList, map sort 사용
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        HashMap<Integer,Double> pairs = new HashMap<Integer,Double>();

        double total = stages.length;

        ArrayList<Integer> list = new ArrayList<>();

        for(int i=0;i<stages.length;i++){
            list.add(stages[i]);
        }

        for(int i=1;i<N+1;i++){
            if (list.contains(i)) {
                double cnt = Collections.frequency(list,i);
                pairs.put(i,(cnt/total));
                total-=cnt;
            }
            else if(!list.contains(i)){
                pairs.put(i,(double)0);
            }
            else if(total==0){
                pairs.put(i,(double)0);
            }
        }

        List<Entry<Integer,Double>> list_entries = new ArrayList<Entry<Integer,Double>>(pairs.entrySet());

        Collections.sort(list_entries, new Comparator<Entry<Integer, Double>>() {
            @Override
            public int compare(Entry<Integer, Double> o1, Entry<Integer, Double> o2) {
                return o2.getValue().compareTo(o1.getValue());
            }
        });

        for(int i=0;i<list_entries.size();i++){
            answer[i] = list_entries.get(i).getKey();
        }

        return answer;
    }

    // solution 2 :
    public int[] solution2(int N, int[] lastStages) {
        int nPlayers = lastStages.length;
        int[] nStagePlayers = new int[N + 2];
        for (int stage : lastStages) {
            nStagePlayers[stage] += 1;
        }

        int remainingPlayers = nPlayers;
        List<Stage> stages = new ArrayList<>();
        for (int id = 1 ; id <= N; id++) {
            double failure = (double) nStagePlayers[id] / remainingPlayers;
            remainingPlayers -= nStagePlayers[id];

            Stage s = new Stage(id, failure);
            stages.add(s);
        }

        Collections.sort(stages, Collections.reverseOrder());

        int[] answer = new int[N];
        for (int i = 0; i < N; i++) {
            answer[i] = stages.get(i).id;
        }
        return answer;
    }

    class Stage implements Comparable<Stage> {
        public int id;
        public double failure;

        public Stage(int id_, double failure_) {
            id = id_;
            failure = failure_;
        }

        @Override
        public int compareTo(Stage o) {
            if (failure < o.failure ) {
                return -1;
            }
            if (failure > o.failure ) {
                return 1;
            }
            return 0;
        }
    }

    public static void main(String[] args) {

        int N = 5;
        int[] stages = {2, 1, 2, 6, 2, 4, 3, 3};

        FailureRate_carnival77 sol = new FailureRate_carnival77();
        sol.solution2(N,stages);

    }

}
