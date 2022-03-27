#include<iostream>
#include<algorithm>
#include<vector>
#include<cstring>
using namespace std;
vector<int> graph[1001];
bool visit[1001];

void dfs(int v) {
	visit[v] = true;
	for (int i = 0; i < graph[v].size(); i++) {
		int next = graph[v][i];
		if (!visit[next]) dfs(next);
	}
}

int main() {
	int ans = 0;
	int n, m;
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		int u, v;
		cin >> u >> v;
		graph[u].push_back(v);
		graph[v].push_back(u);
	}
	memset(visit, false, sizeof(visit));
	// 노드 번호가 1부터 삽입되었으니, 1부터 탐색해야한다! 그리고 v번까지 노드가 있으니, 탐색 범위는 i <= n 이다.
	for (int i = 1; i <= n; i++) {
		if (!visit[i]) {
			ans += 1;
			dfs(i);
		}
	}

	cout << ans << '\n';
	return 0;
}