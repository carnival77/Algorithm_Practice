//풀이
//1. 행동 3가지(x+1,x-1,2x) 모두 0 or 1초씩 소요되므로 BFS 로 풀이 가능
//2. 위치 = 정점. 이동 가능한 경우의 수 = 위치 간의 간선.
//3. 시간복잡도 : 정점 1개(10만) + 간선 2개(20만) = 30만. O(40만). 2초 내에 풀이 가능.
//4. 정점의 범위 : 0~10만. 그러므로 2*X 하는 순간이동을 고려하면 최대 탐색 범위는 20만
//5. 순간이동의 경우 0초가 걸린다. 즉, 각 행동들이 0 or 1초가 소요되므로
//		덱을 사용한다. 초를 단위로 앞뒤로 넣는다. 0초는 push_front, 1초는 push_back을 한다. 

#include<iostream>
#include<deque>
#include<algorithm>
using namespace std;
const int MAX = 1000000;
bool check[MAX];
int dist[MAX];

int main() {
	deque<int> q;
	int n, k;
	cin >> n >> k;
	q.push_front(n);
	dist[n] = 0;
	check[n] = true;
	while (!q.empty()) {
		int now, next;
		now = q.front(); q.pop_front();
		if (2 * now < MAX) {
			next = 2 * now;
			if (check[next] == false) {
				check[next] = true;
				dist[next] = dist[now];
				q.push_front(next);
			}
		}
		if (now + 1 < MAX) {
			next = now + 1;
			if (check[next] == false) {
				check[next] = true;
				dist[next] = dist[now]+1;
				q.push_back(next);
			}
		}
		if (now -1 >= 0 ) {
			next = now -1 ;
			if (check[next] == false) {
				check[next] = true;
				dist[next] = dist[now] + 1;
				q.push_back(next);
			}
		}
	}

	cout << dist[k];

	return 0;
}