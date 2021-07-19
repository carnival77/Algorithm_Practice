package ∫ŒµÓ»£_2529;

import java.util.*;
public class Main {
	static int k;
	static boolean[] used = new boolean[10];
	static ArrayList<String> ans = new ArrayList<String>();
	static char[] arr = new char[9];
	
	static boolean check(String num, int k) {
		for (int i=0; i<k;i++) {
			if (arr[i] == '<') {
				if (num.charAt(i)>num.charAt(i+1)) return false;
			}
			else if (arr[i] == '>') {
				if (num.charAt(i)<num.charAt(i+1)) return false;
			}
		}
		return true;
	}
	
	static boolean good(char op, char x, char y) {
		if (op == '<') {
			if (x>y) return false;
		}
		else if ( op == '>') {
			if (x<y)return false;
		}
		
		return true;
	}
	
	static void recur(int index, String num, int k) {
		if (index == k+1) {
			if (check(num,k)) {
				ans.add(num);
			}
			return;
		}
		
		for (int i=0;i<10;i++) {
			if (used[i]) continue;
			if (index == 0 || good(arr[index-1], (char)(i-'0'),num.charAt(index-1))) {
				used[i] = true;
				recur(index+1,num+Integer.toString(i),k);
				used[i] = false;
			}
		}
	}
	
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		k=sc.nextInt();
		for (int i=0;i<k;i++) {
			arr[i] = sc.next().toCharArray()[0];
		}
		recur(0,"",k);
		Collections.sort(ans);
		int m = ans.size();
		System.out.println(ans.get(m-1));
		System.out.println(ans.get(0));
	}
}
