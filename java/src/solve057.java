
/*
 * 백준 11654 아스키 코드
 * 파이썬에서 풀고 자바로 어떻게하나 궁금해져서 풀이 :)
*/

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class solve057 {
	public static int solution(char c) {
		
		int answer = (int) c; 
		
		return answer;
		
	}
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		char c = br.readLine().charAt(0);
		
		System.out.println(solution(c));
	}
}
