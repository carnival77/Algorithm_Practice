#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int s[20][20];
int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> s[i][j];
		}
	}
	int ans = -1;
	// n까지의 수로 만들 수 있는 모든 이진수 경우의 수를 탐색한다. 즉, n명까지의 각 번호의 사람이 참석하는 지(1) 안 하는 지(0)를 구분한 모든 경우의 수이다.
	for (int i = 0; i < (1 << n); i++) {
		int cnt = 0;
		// 백트랙킹 종료 조건 1 : 전체 수가 n/2 가 아닐 경우 무시
		// n/2 명이 참여한 경우의 수만 선별한다. 0부터 n까지의 이진수를 탐색하여, 참석한 명수를 cnt로 증가시키고, cnt가 n/2일 때만 계속 진행한다.
		for (int k = 0; k<n; k++) {
			if (i & (1 << k)) cnt++;
		}
		if (cnt != n / 2) continue;
		// 두 팀 선언 
		vector<int> first, second;
		// 두 팀에 인원 삽입
		// n명 중 이번 i 이진수 경우의 수에 선택된 사람이 있는 지 n까지의 for문으로 탐색하여, 있다면 first에, 없다면 second에 넣는다.
		// 가령  i : 1010(2)라면, (0번, 2번)의 사람들만 first에 삽입되고 나머지 (1번, 3번) 의 사람들은 second에 삽입된다.
		for (int k = 0; k < n; k++) {
			if (i & (1 << k)) first.push_back(k);
			else { second.push_back(k); }
		}
		//// 백트랙킹 종료조건 2 : 집합 요소 수가 n/2가 아닐 경우 무시
		//if (first.size() != n / 2) continue;

		int t1 = 0;
		int t2 = 0;
		// 각 팀의 능력치의 합을 구한다.
		for (int a = 0; a < n / 2; a++) {
			for (int b = 0; b < n / 2; b++) {
				if (a == b) continue;
				t1 += s[first[a]][first[b]];
				t2 += s[second[a]][second[b]];
			}
		}
		int diff = t1 - t2;
		if (diff < 0) diff = -diff;
		if (ans == -1 || ans > diff) ans = diff;
	}
	cout << ans << '\n';
}