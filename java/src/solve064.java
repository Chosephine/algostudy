import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/*
 * 백준 1929 소수 구하기 
 * https://www.acmicpc.net/problem/1929
 */

public class solve064 {
	// ver.1 숫자 개별적으로 소수판별 : 시간초과 
	public static boolean isPrime(int number) {
		boolean answer = true;
		
		for (int i = number - 1; i > 1; i--) {
			if (number % i == 0) {
				answer = false;
				break;
			}
		}
			
		return answer;
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		int start = Integer.parseInt(st.nextToken());
		int end = Integer.parseInt(st.nextToken());
		
		// ver.1 start~end 순회하며 개별 숫자 소수 여부 파악 : 시간초과 
		for (int n = start; n < end + 1; n++) {
			
			if (isPrime(n)) {
			 	
				sb.append(n);
			 	sb.append('\n');
			 	
			}
			
		}
		
		System.out.println(sb);
		
	}
	
}
