#include<iostream>
#include<string>
using namespace std;
struct Queue {
	int arr[10000];
	int begin, end;
	Queue() {
		begin = 0;
		end = 0;
	}
	void push(int n) {
		arr[end] = n;
		end++;
	}
	bool empty() {
		if (begin == end) {
			return true;
		}
		else {
			return false;
		}
	}
	int pop() {
		if (empty()) return -1;
		begin++;
		return arr[begin - 1];
	}
	int size() {
		return end - begin;
	}
	int front() {
		if (empty()) return -1;
		else return arr[begin];
	}
	int back() {
		if (empty()) return -1;
		else return arr[end - 1];
	}
};

int main() {
	int a;
	cin >> a;
	int n;
	Queue q;
	for (int i = 0; i < a; i++) {
		string cmd;
		cin >> cmd;
		if (cmd == "push") {
			cin >> n;
			q.push(n);
		}
		else if (cmd == "front") cout << q.front() << '\n';
		else if (cmd == "back") cout << q.back() << '\n';
		else if (cmd == "size") cout << q.size() << '\n';
		else if (cmd == "empty") {
			if (q.empty()) cout << "1" << '\n';
			else cout << "0" << '\n';
		}
		else if (cmd == "pop") {
			cout << q.pop() << '\n';
		}
	}
	return 0;
}