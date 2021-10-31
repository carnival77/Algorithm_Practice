package programmers.level02.printer;
import programmers.level02.phoneNumList.PhoneNumList_carnival77;
// 우선순위 큐 사용해볼 것
import java.awt.*;
import java.util.*;
public class Printer_carnival77 {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        int print=0;

        Queue<Point> queue = new LinkedList<Point>();

        for(int i=0;i<priorities.length;i++){
            queue.offer(new Point(priorities[i],i));
        }

        while(queue.size()>0){
            Point tg = new Point();
            tg = queue.poll();
            int max_pr = 0;
            if(queue.size()>0){
                for(Point p : queue){
                    max_pr = Math.max(max_pr,p.x);
                }
                if(tg.x < max_pr){
                    queue.offer(tg);
                }
                else{
                    print = print+1;
                    if(location == tg.y){
                        answer=print;
                        return answer;
                    }
                }
            }
            else{
                print = print+1;
                if(location == tg.y){
                    answer=print;
                    return answer;
                }
            }
        }


        return answer;
    }

    public int solution2(int[] priorities, int location) {
        int answer = 1;

        PriorityQueue<Integer> q = new PriorityQueue<>(Collections.reverseOrder());

        for(int p : priorities){
            q.add(p);
        }

        while(!q.isEmpty()){
            for(int i=0;i<priorities.length;i++){
                if(priorities[i] == q.peek()){
                    if(location == i){
                        return answer;
                    }
                    answer+=1;
                    q.poll();
                }
            }
        }
        return answer;
    }

    public static void main(String[] args) {

        int[] priorities = {2, 1, 3, 2};
        int location = 2;

        Printer_carnival77 sol = new Printer_carnival77();
        System.out.println(sol.solution2(priorities,location));
    }
}
