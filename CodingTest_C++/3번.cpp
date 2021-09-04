//3.	3번
//A.유형 : 브루트 포스 – 재귀
//B.지문 : 징검다리와 개구리가 있다.징검다리는[4, 1, 2, 3, 1, 0, 5] 와 같은 형태이며, 목표는 마지막 돌에 도달하는 것이다.각 징검다리에 적힌 숫자만큼 이동 가능하다.첫 돌부터 시작하며, 각 돌에서 앞이나 뒤로 이동할 수 있다.마지막 돌에 도달하기 위한 최소 이동 횟수를 구하라.만약 마지막 돌에 도달 못 한다면 - 1을 반환하라.

// 재귀로 풀려고 했으나, 안 풀어져서 while문으로 바꿨다.

#include<vector>
#include<algorithm>
#include<iostream>
using namespace std;

int solution(vector<int> &nums) {
	int answer = -1;
	int cnt = 0;
	int len = nums.size();
	int last = len - 1;
	int cur_index = nums[0];

	while (true) {
		// 종료 조건
		// 1. 처음 돌로 되돌아오면
		if (cur_index == 0) return -1;
		// 2. 마지막 돌에 도달하면
		if (cur_index == last) {
			if (cnt > answer) {
				answer = cnt;
				return answer;
			}
		}
		// 3. 지금 돌의 값이 0이라면
		if (nums[cur_index] == 0) {
			return -1;
		}
		// 전진
		int next_index = cur_index + nums[cur_index];
		// 전진 가능하면
		if (next_index < len) {
			// 전진
			cur_index = next_index;
			cnt++;
		}
		else { continue; }
		// 후진
		next_index = cur_index - nums[cur_index];
		// 후진 가능하면
		if (next_index > 0) {
			// 후진
			cur_index = next_index;
			cnt++;
		}
		else { continue; }
	}


	return answer;
}

int main() {
	vector<int> nums;
	nums.push_back(4);
	nums.push_back(1);
	nums.push_back(2);
	nums.push_back(3);
	nums.push_back(1);
	nums.push_back(0);
	nums.push_back(5);

	int ans = solution(nums);

	cout << ans << '\n';

	return ans;
}