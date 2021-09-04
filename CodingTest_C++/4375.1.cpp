#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

int main() {
	int test[3];
	cin >> test[0] >> test[1] >> test[2];

	for (int i = 0; i < sizeof(test) / sizeof(int); i++) {
		bool pass = true;
		int n = 1;
		int tmp = 0;
		int cnt = 0;
		while (pass) {
			cnt = 0;
			tmp = test[i] * n;
			string tmp_str = to_string(tmp);
			for (int j = 0; j < tmp_str.length(); j++) {
				if (tmp_str.at(j) == '1') {
					cnt++;
				}
				else break;
			}
			n++;
			if (cnt == tmp_str.length()) {
				pass = false;
				break;
			}
		}
		cout << cnt << '\n';
	}


	return 0;
}