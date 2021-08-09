//풀이
// 1. 행동 3가지(x+1,x-1,2x) 모두 1초씩 소요되므로 BFS 로 풀이 가능
// 2. 위치 = 정점. 이동 가능한 경우의 수 = 위치 간의 간선.
// 3. 시간복잡도 : 정점 1개(10만) + 간선 3개(30만) = 40만. O(40만). 2초 내에 풀이 가능.
// 4. 정점의 범위 : 0~10만. 그러므로 2*X 하는 순간이동을 고려하면 최대 탐색 범위는 20만
// 5. 이동 경로 : from[next] = now 를 사용해서 역순으로 추론해야 한다.
// 6. from : 이전에 있던 위치를 저장하는 배열. from[x] 는 x로 가기 전 위치를 나타낸다.
// 7. n 부터 m 까지 간다고 하면, 이것은 n부터 from[m] 까지 간 다음 from[m] 에서 m으로 가는 것과 같다.

#include<iostream>
#include<queue>
#include<cstring>
#include<algorithm>
using namespace std;
vector<int> graph[200001];
bool check[200001];
int dist[200001];
int from[200001];

void print_sp(int n, int m) {
	if (n != m) {
		print_sp(n, from[m]);
	}
	cout << m << ' ';
}

int main() {
	memset(check, false, sizeof(check));
	memset(dist, -1, sizeof(dist));
	memset(from, -1, sizeof(from));
	int n, k;
	cin >> n >> k;
	int ans = 1e9;

	queue<int> q;
	check[n] = true;
	dist[n] = 0;
	q.push(n);
	int now;
	int next;

	while (!q.empty()) {
		now = q.front(); q.pop();
		if (now - 1 >= 0) {
			next = now - 1;
			if (check[next] == false) {
				check[next] = true;
				dist[next] = dist[now] + 1;
				from[next] = now;
				q.push(next);
			}
		}
		if (now + 1 < 200000) {
			next = now + 1;
			if (check[next] == false) {
				check[next] = true;
				dist[next] = dist[now] + 1;
				from[next] = now;
				q.push(next);
			}
		}
		if (2 * now < 200000) {
			next = 2 * now;
			if (check[next] == false) {
				check[next] = true;
				dist[next] = dist[now] + 1;
				from[next] = now;
				q.push(next);
			}
		}
	}

	ans = dist[k];
	cout << ans <<'\n';;

	print_sp(n, k);

	return 0;
}