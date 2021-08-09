//Ǯ��
// 1. �ൿ 3����(x+1,x-1,2x) ��� 1�ʾ� �ҿ�ǹǷ� BFS �� Ǯ�� ����
// 2. ��ġ = ����. �̵� ������ ����� �� = ��ġ ���� ����.
// 3. �ð����⵵ : ���� 1��(10��) + ���� 3��(30��) = 40��. O(40��). 2�� ���� Ǯ�� ����.
// 4. ������ ���� : 0~10��. �׷��Ƿ� 2*X �ϴ� �����̵��� ����ϸ� �ִ� Ž�� ������ 20��
// 5. �̵� ��� : from[next] = now �� ����ؼ� �������� �߷��ؾ� �Ѵ�.
// 6. from : ������ �ִ� ��ġ�� �����ϴ� �迭. from[x] �� x�� ���� �� ��ġ�� ��Ÿ����.
// 7. n ���� m ���� ���ٰ� �ϸ�, �̰��� n���� from[m] ���� �� ���� from[m] ���� m���� ���� �Ͱ� ����.

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