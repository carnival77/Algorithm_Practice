#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int cal(vector<int>& a) {
	int result = 0;
	for (int i = 1; i < a.size(); i++) {
		result += abs(a[i - 1] - a[i]);
	}
	return result;
}
int main() {
	int n;
	int ans=0;
	cin >> n;
	vector<int> a(n);
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	sort(a.begin(), a.end());
	do {
		int temp = cal(a);
		ans = max(ans,temp);
	} while (next_permutation(a.begin(), a.end()));
	cout << ans << '\n';
	return 0;
}