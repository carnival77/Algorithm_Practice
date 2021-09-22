#include<iostream>
#include<algorithm>
#include<vector>
#include<stdio.h>
using namespace std;
int main() {
	int n;
	int ans = 1e9;
	int s[10][10];
	scanf_s("%d", &n);
	vector<int> a(n);
	for (int i = 0; i < n; i++) {
		a[i] = i;
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf_s("%d",&s[i][j]);
		}
	}
	do {
		bool pass = true;
		int sum = 0;
		for (int i = 1; i < n; i++) {
			if (s[a[i - 1]][a[i]] == 0) pass = false;
			else sum += s[a[i - 1]][a[i]];
		}
		if (pass && s[a[n - 1]][a[0]] != 0) {
			sum += s[a[n - 1]][a[0]];
			ans = min(ans, sum);
		}
	} while (next_permutation(a.begin(), a.end()));
	cout << ans << '\n';
	return 0;
}