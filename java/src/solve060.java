
/*
 * 백준 2292 벌집 
 * https://www.acmicpc.net/problem/2292
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class solve060 {
	public static int solution(int N){
			
		int answer = 1;
		if (N != 1) {
			
			int limit = (int)(1000000000/6);
			
			for (int i = 1; i < limit ; i++) {
				
				answer += 1;
				
				if (N > 1 + 3 * ((i - 1) * i) && N <= 1 + 3 * (i*(i + 1))) {	
					break;
				}
			}
		}
		
		return answer;
	}
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		System.out.println(solution(N));
		
	}

}
