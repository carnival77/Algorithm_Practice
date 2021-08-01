#include<algorithm>
#include<iostream>
#include<vector>
#include <queue>
using namespace std;
vector<int> graph[1001];
bool check[1001];

void dfs(int v) {
	check[v] = true;
	printf("%d ", &v);
	for (int i = 0; i < graph[v].size(); i++) {
		int next = graph[v][i];
		if (check[next] == false) dfs(next);
	}
}

void bfs(int v) {
	memset(check, false, sizeof(check));
	queue<int> q;
	check[v] = true;
	q.push(v);
	while (q.empty()) {
		v = q.front(); q.pop();
		printf("%d ", &v);
		for (int i = 0; i < graph[v].size(); i++) {
			int next = graph[v][i];
			if (check[next] == false) {
				check[next] = true;
				q.push(next);
			}
		}
	}

}

int main() {
	int n, m, start;
	cin >> n >> m >> start;
	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		graph[a].push_back(b);
		graph[b].push_back(a);
	}
	memset(check, false, sizeof(check));
	for (int i = 0; i < n; i++) { 
		sort(graph[i].begin(), graph[i].end());
	}
	dfs(start);
	cout << '\n';
	bfs(start);
	cout << '\n';

	return 0;
}