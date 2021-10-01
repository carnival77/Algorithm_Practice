//Ǯ��
//1. �ൿ 3����(x+1,x-1,2x) ��� 1�ʾ� �ҿ�ǹǷ� BFS �� Ǯ�� ����
//2. ��ġ = ����. �̵� ������ ����� �� = ��ġ ���� ����.
//3. �ð����⵵ : ���� 1��(10��) + ���� 3��(30��) = 40��. O(40��). 2�� ���� Ǯ�� ����.
//4. ������ ���� : 0~10��. �׷��Ƿ� 2*X �ϴ� �����̵��� ����ϸ� �ִ� Ž�� ������ 20��

#include<iostream>
#include<queue>
#include<cstring>
#include<algorithm>
using namespace std;
bool check[200001];
int dist[200001];

int main() {
	memset(check, false, sizeof(check));
	memset(dist, -1, sizeof(dist));
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
		if (now + 1 < 200000) {
			next = now + 1;
			if (check[next] == false) {
				check[next] = true;
				dist[next] = dist[now] + 1;
				q.push(next);
			}
		}
		if (2*now < 200000) {
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