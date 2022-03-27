//풀이
//1. 행동 3가지(x+1,x-1,2x) 모두 0 or 1초씩 소요되므로 BFS 로 풀이 가능
//2. 위치 = 정점. 이동 가능한 경우의 수 = 위치 간의 간선.
//3. 시간복잡도 : 정점 1개(10만) + 간선 2개(20만) = 30만. O(40만). 2초 내에 풀이 가능.
//4. 정점의 범위 : 0~10만. 그러므로 2*X 하는 순간이동을 고려하면 최대 탐색 범위는 20만
//5. 순간이동의 경우 0초가 걸린다. 즉, 각 행동들이 0 or 1초가 소요되므로
//		큐를 now_q, next_q 를 쓴다. 순간이동을 제외한 행동들은 next_q를 사용한다.
//		큐는 초 단위로 사용되며, 해당 초의 요소를 다 썼으면 다음 초의 큐로 갱신된다.

#include <iostream>
#include <queue>
#include <deque>
using namespace std;
bool c[1000000];
int d[1000000];
int MAX = 1000000;
int main() {
    int n, m;
    cin >> n >> m;
    c[n] = true;
    d[n] = 0;
    queue<int> q;
    queue<int> next_queue;
    q.push(n);
    while (!q.empty()) {
        int now = q.front();
        q.pop();
        if (now * 2 < MAX) {
            if (c[now * 2] == false) {
                q.push(now * 2);
                c[now * 2] = true;
                d[now * 2] = d[now];
            }
        }
        if (now - 1 >= 0) {
            if (c[now - 1] == false) {
                next_queue.push(now - 1);
                c[now - 1] = true;
                d[now - 1] = d[now] + 1;
            }
        }
        if (now + 1 < MAX) {
            if (c[now + 1] == false) {
                next_queue.push(now + 1);
                c[now + 1] = true;
                d[now + 1] = d[now] + 1;
            }
        }
        if (q.empty()) {
            q = next_queue;
            next_queue = queue<int>();
        }
    }
    cout << d[m] << '\n';
    return 0;
}