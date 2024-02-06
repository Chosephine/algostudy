import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/*
 * 백준 2609 최대공약수와 최소공배수
 * https://www.acmicpc.net/problem/2609
*/

public class solve066 {
	
	// 소수 판별을 위한 에라토스의 체 변형해서 사용
	// 1은 소수는 아니지만 약수는 될 수 있으므로 true
	public static void eratos(boolean[] arr) {
		
		arr[0] = false;
		
		for (int i = 2; i < arr.length; i ++) {
			
			if (arr[i]) {
				
				for (int j = 2; i * j < arr.length; j ++) {
					arr[i * j] = false;
				}
				
			}
			
		}
		
	}
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n1 = Integer.parseInt(st.nextToken());
		int n2 = Integer.parseInt(st.nextToken());
		
		// 소수 판별을 위한 prime 배열 생성
		int min = Integer.min(n1, n2);
		boolean[] prime = new boolean[min + 1];
		Arrays.fill(prime, true);
		eratos(prime);
		
		// 최대공악수 계산
		int gcd = 1;
		for (int i = 2; i < min + 1; i++) {
			
			while (true) {
				
				if (prime[i] & n1 % i == 0 & n2 % i == 0) {
					
					gcd *= i;
					n1 /= i;
					n2 /= i;
					
				}
				else break;
			}
			
		}
		
		System.out.println(gcd);
		System.out.println(gcd * n1 * n2);
		
	}

}
