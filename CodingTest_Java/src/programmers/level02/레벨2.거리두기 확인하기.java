package programmers.level02.distanceCheck;

import java.util.*;

class Pair{
    int x;
    int y;
    int dist;

    Pair(int x, int y, int dist){
        this.x=x;
        this.y=y;
        this.dist=dist;
    }
}

public class DistanceCheck_carnival77 {

    public static int[] dx={-1,1,0,0};
    public static int[] dy={0,0,-1,1};

    public static int[] solution(String[][] places) {
        int[] answer = new int[5];
        int inx=0;

        for(String[] place : places){
            boolean safe = true;
            for(int i=0;i<5;i++){
                for(int j=0;j<5;j++){
                    if(place[i].charAt(j) == 'P'){
                        if(!bfs(i,j,place)){
                            safe=false;
                            break;
                        }
                    }
                }
                if (safe==false)
                    break;
            }
            if(safe==false)
                answer[inx]=0;
            else
                answer[inx]=1;
            inx+=1;
        }

        return answer;
    }
    public static boolean bfs(int x,int y,String[] place) {
        Queue<Pair> q = new LinkedList<>();
        int dist=0;
        q.add(new Pair(x,y,dist));
        boolean[][] visited = new boolean[5][5];
        visited[x][y]=true;

        while(!q.isEmpty()){
            Pair p = q.remove();
            x=p.x;
            y=p.y;
            dist=p.dist;
            for(int k=0;k<4;k++){
                int nx=x+dx[k];
                int ny=y+dy[k];
                if(0<=nx && nx<5 && 0<=ny && ny<5 && !visited[nx][ny]){
                    if(place[nx].charAt(ny)=='O' && dist<1){
                        q.add(new Pair(nx,ny,dist+1));
                        visited[nx][ny]=true;
                    }
                    else{
                        if(place[nx].charAt(ny)=='P'){
                            return false;
                        }
                    }
                }
            }
        }


        return true;
    }

    public static void main(String[] args) {

        String[][] places = {{"POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"},
                {"POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"},
                {"PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"},
                {"OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"},
                {"PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"}};

        DistanceCheck_carnival77 sol = new DistanceCheck_carnival77();
        int[] answer = sol.solution(places);

        for(int ans : answer){
            System.out.println(ans);
        }

    }
}
