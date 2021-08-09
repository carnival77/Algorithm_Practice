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