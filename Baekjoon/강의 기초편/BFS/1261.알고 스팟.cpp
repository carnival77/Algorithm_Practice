#include<iostream>
#include<deque>
#include<algorithm>
#include<cstdio>
using namespace std;

int d[555][555];
int a[555][555];
int dx[4] = { 1,-1,0,0 };
int dy[4] = { 0,0,1,-1 };

int main() {
	int n, m;
	scanf("%d %d", &m, &n);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%1d", &a[i][j]);
			d[i][j] = -1;
		}
	}
	deque<pair<int, int>> q;
	q.push_back(make_pair(0,0));
	d[0][0] = 0;
	while (!q.empty()) {
		
		int x = q.front().first;
		int y = q.front().second;
		q.pop_front();
		
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (0 <= nx && nx < n && 0 <= ny && ny < m) {
				if (d[nx][ny] == -1) {
					if (a[nx][ny] == 0) {
						d[nx][ny] = d[x][y];
						q.push_front(make_pair(nx, ny));
					}
					else{
						d[nx][ny] = d[x][y] + 1;
						q.push_back(make_pair(nx, ny));
					}
				}
			}
		}
	}

	printf("%d\n", d[n - 1][m - 1]);

	return 0;
}