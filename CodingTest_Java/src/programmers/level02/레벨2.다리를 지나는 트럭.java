package programmers.level02.truckCrossingBridge;

import java.util.*;

public class TruckCrossingBridge_carnival77 {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0; // 다리에 트럭을 추가할 때 증가

        int cur=0; // 현재 무게

        Queue<Integer> q = new LinkedList<>(); // 다리에 있는 트럭

        // 트럭 하나하나씩
        for(int truck : truck_weights){
            // 각 트럭이 다리를 지나는 시간을 구하기 위해 while문으로.
            while(true){
                // 1번 : 다리에 트럭이 없을 경우
                if(q.isEmpty()){
                    // 다리에 트럭이 가게 한다.
                    q.add(truck);
                    cur+=truck;
                    answer+=1;
                    break;
                }
                // 2번 : 다리에 트럭이 꽉 찼을 경우
                else if(bridge_length == q.size()){
                    // 맨 앞 트럭 하나를 빼 준다
                    cur-=q.poll();
                }
                // 3번 : 다리에 트럭이 수용 가능한 개수만 존재할 경우
                else{
                    // 현재 무게에 이번 트럭 무게를 더한 결과가 한계치 이하일 경우
                    if(cur+truck <= weight){
                        // 다리에 트럭 추가
                        q.add(truck);
                        cur+=truck;
                        answer+=1;
                        break;
                    }
                    // 현재 무게에 이번 트럭 무게를 더한 결과가 한계치를 초과할 경우
                    else{
                        // 다리에 있는 트럭 개수를 임의로 1개 증가시켜, 2번으로 가서 맨 앞 트럭을 하나 빼 주도록 한다.
                        q.add(0);
                        answer+=1;
                    }
                }
            }
        }
        // 맨 마지막 트럭이 다리를 지나가는 시간 더해주기
        return answer + bridge_length;
    }

    // solution 2: truck class , waitQ, moveQ 활용.

    class Truck {
        int weight;
        int move;

        public Truck(int weight) {
            this.weight = weight;
            this.move = 1;
        }

        public void moving() {
            move++;
        }
    }

    public int solution2(int bridgeLength, int weight, int[] truckWeights) {
        Queue<Truck> waitQ = new LinkedList<>();
        Queue<Truck> moveQ = new LinkedList<>();

        for (int t : truckWeights) {
            waitQ.offer(new Truck(t));
        }

        int answer = 0;
        int curWeight = 0;

        while (!waitQ.isEmpty() || !moveQ.isEmpty()) {
            answer++;

            if (moveQ.isEmpty()) {
                Truck t = waitQ.poll();
                curWeight += t.weight;
                moveQ.offer(t);
                continue;
            }

            for (Truck t : moveQ) {
                t.moving();
            }

            if (moveQ.peek().move > bridgeLength) {
                Truck t = moveQ.poll();
                curWeight -= t.weight;
            }

            if (!waitQ.isEmpty() && curWeight + waitQ.peek().weight <= weight) {
                Truck t = waitQ.poll();
                curWeight += t.weight;
                moveQ.offer(t);
            }
        }

        return answer;
    }
}
