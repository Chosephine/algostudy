import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/*
 * 백준 11050 이항 계수 1
 * https://www.acmicpc.net/problem/11050
*/

public class solve067 {
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		int denominator = 1;
		int numerator = 1;
		
		for (int i = 1; i <= K; i++) {
			
			denominator *= (N + 1 - i);
			numerator *= i;
			
		}
		
		System.out.println(denominator / numerator);
	}
}
