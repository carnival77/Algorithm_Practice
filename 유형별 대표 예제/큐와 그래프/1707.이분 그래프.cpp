//풀이
//1. 두 그룹을 분류하기 위해 visit 대신 color 라는 것을 쓴다.
//1.1. color에는 0,1,2 가 들어간다. 0 = 미방문, 1 = 그룹 1, 2 = 그룹 2
//1.2. next node를 할 때, 3-c를 한다.
//2. 만약 이번 node 와 next node의 color가 같다면 false다.

#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>
#include<cstring>
using namespace std;
vector<int> graph[20001];
int color[20001];

bool dfs(int node, int c) {
	color[node] = c;
	for (int i = 0; i < graph[node].size(); i++) {
		int next = graph[node][i];
		if (color[next] == 0) {
			if (dfs(next, 3 - c) == false) {
				return false;
			}
		}
		else if (color[next] == color[node]) {
			return false;
		}
	}
	return true;
}

int main() {
	int k;
	cin >> k;
	for (int i = 0; i < k; i++) {
		int v, e;
		cin >> v >> e;
		// graph, color 초기화. 여기서 중요한 점은 노드 번호 기준이므로 탐색 범위는 1 <= a <= v
		for (int a = 1; a <= v; a++) {
			graph[a].clear();
			color[a] = 0;
		}
		for (int j = 0; j < e; j++) {
			int start, end;
			cin >> start >> end;
			graph[start].push_back(end);
			graph[end].push_back(start);
		}
		bool ans = true;
		// 여기서 중요한 점은 노드 번호 기준이므로 탐색 범위는 1 <= q <= v
		for (int q = 1; q <= v; q++) {
			if (color[q] == 0) {
				if (dfs(q, 1) == false) {
					ans = false;
				}
			}
		}
		if (ans == true) cout << "YES\n";
		else if(ans==false) cout << "NO\n";
	}
	return 0;
}