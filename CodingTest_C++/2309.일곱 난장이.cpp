#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
	int n = 9;
	int arr[9];
	int sum = 0;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
		sum += arr[i];
	}
	sort(arr, arr + n);
	for (int i = 0; i < n; i++) {
		for (int j = 1; j < n; j++) {
			if ((sum - arr[i] - arr[j]) == 100) {
				for (int k = 0; k < n; k++) {
					if (k == i || k == j) {
						continue;
					}
					else {
						cout << arr[k] << '\n';
					}
				}
				return 0;
			}
		}
	}

	return 0;
}