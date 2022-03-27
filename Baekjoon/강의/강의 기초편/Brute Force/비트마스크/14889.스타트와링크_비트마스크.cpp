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
	// n������ ���� ���� �� �ִ� ��� ������ ����� ���� Ž���Ѵ�. ��, n������� �� ��ȣ�� ����� �����ϴ� ��(1) �� �ϴ� ��(0)�� ������ ��� ����� ���̴�.
	for (int i = 0; i < (1 << n); i++) {
		int cnt = 0;
		// ��Ʈ��ŷ ���� ���� 1 : ��ü ���� n/2 �� �ƴ� ��� ����
		// n/2 ���� ������ ����� ���� �����Ѵ�. 0���� n������ �������� Ž���Ͽ�, ������ ����� cnt�� ������Ű��, cnt�� n/2�� ���� ��� �����Ѵ�.
		for (int k = 0; k<n; k++) {
			if (i & (1 << k)) cnt++;
		}
		if (cnt != n / 2) continue;
		// �� �� ���� 
		vector<int> first, second;
		// �� ���� �ο� ����
		// n�� �� �̹� i ������ ����� ���� ���õ� ����� �ִ� �� n������ for������ Ž���Ͽ�, �ִٸ� first��, ���ٸ� second�� �ִ´�.
		// ����  i : 1010(2)���, (0��, 2��)�� ����鸸 first�� ���Եǰ� ������ (1��, 3��) �� ������� second�� ���Եȴ�.
		for (int k = 0; k < n; k++) {
			if (i & (1 << k)) first.push_back(k);
			else { second.push_back(k); }
		}
		//// ��Ʈ��ŷ �������� 2 : ���� ��� ���� n/2�� �ƴ� ��� ����
		//if (first.size() != n / 2) continue;

		int t1 = 0;
		int t2 = 0;
		// �� ���� �ɷ�ġ�� ���� ���Ѵ�.
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