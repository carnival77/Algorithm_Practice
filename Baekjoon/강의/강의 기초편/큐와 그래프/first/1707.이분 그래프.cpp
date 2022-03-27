//Ǯ��
//1. �� �׷��� �з��ϱ� ���� visit ��� color ��� ���� ����.
//1.1. color���� 0,1,2 �� ����. 0 = �̹湮, 1 = �׷� 1, 2 = �׷� 2
//1.2. next node�� �� ��, 3-c�� �Ѵ�.
//2. ���� �̹� node �� next node�� color�� ���ٸ� false��.

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
		// graph, color �ʱ�ȭ. ���⼭ �߿��� ���� ��� ��ȣ �����̹Ƿ� Ž�� ������ 1 <= a <= v
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
		// ���⼭ �߿��� ���� ��� ��ȣ �����̹Ƿ� Ž�� ������ 1 <= q <= v
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