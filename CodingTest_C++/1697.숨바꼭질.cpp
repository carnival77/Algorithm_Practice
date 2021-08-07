//풀이
//1. 행동 3가지(x+1,x-1,2x) 모두 1초씩 소요되므로 BFS 로 풀이 가능
//2. 위치 = 정점. 이동 가능한 경우의 수 = 위치 간의 간선.
//3. 시간복잡도 : 정점 1개(10만) + 간선 3개(30만) = 40만. O(40만). 2초 내에 풀이 가능.


#include<iostream>
#include<queue>
#include<cstring>
#include<algorithm>
using namespace std;
vector<int> graph[200001];
bool check[200001];
int dist[200001];

int main() {
	memset(check, false, sizeof(check));
	memset(dist, -1, sizeof(check));
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
			next = now -1;
			if (check[next] == false) {
				check[next] = true;
				dist[next] = dist[now] + 1;
				q.push(next);
			}
		}
		if (now + 1 <= 200000) {
			next = now + 1;
			if (check[next] == false) {
				check[next] = true;
				dist[next] = dist[now] + 1;
				q.push(next);
			}
		}
		if (2*now <= 200000) {
			next = 2*now;
			if (check[next] == false) {
				check[next] = true;
				dist[next] = dist[now] + 1;
				q.push(next);
			}
		}
	}

	ans = dist[k];
	cout << ans;;

	return 0;
}